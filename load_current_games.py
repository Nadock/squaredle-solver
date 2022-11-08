#!/usr/bin/env python
"""
Reads the current Squaredle game via their API and write the game and corresponding
words list to the `./games` directory.

This relies on a lot of reverse engineered implementation details so it will almost
certainly break very quickly.
"""
import base64
import json
import os
import pathlib
import sys

import requests

PUZZLE_CONFIG_URL = "https://squaredle.app/api/today-puzzle-config.js"


def decrypt_b64(cyphertext: str) -> str:
    plain_b64 = decrypt_text(cyphertext)
    content = base64.b64decode(plain_b64)
    return content.decode("utf-8")


def decrypt_text(text: str) -> str:
    key = list("5pyf0gcrl1a9oe3ui8d2htn67sqjkxbmw4vzPYFGCRLAOEUIDHTNSQJKXBMWVZ")

    def shift_char(char: str):
        try:
            return key[(key.index(char) - 12 + len(key)) % len(key)]
        except ValueError:
            return char

    return "".join([shift_char(char) for char in text])


def load_puzzle_config() -> dict:
    puzzle_js_response = requests.get(
        PUZZLE_CONFIG_URL, timeout=float(os.environ.get("SQUAREDLE_TIMEOUT", 10.0))
    )
    puzzle_js_response.raise_for_status()

    puzzle_lines = []
    start_found = False
    for bline in puzzle_js_response.iter_lines():
        line = bline.decode("utf-8")
        if start_found or "var gPuzzleConfig =" in line:
            start_found = True
            puzzle_lines.append(line)

    # Drop last 3 lines
    puzzle_lines = puzzle_lines[:-3]

    # Remove JS specific noise
    puzzle_lines[0] = puzzle_lines[0].replace("var gPuzzleConfig =", "")
    puzzle_lines[-1] = puzzle_lines[-1].replace(";", "")

    return json.loads("\n".join(puzzle_lines))


def parse_puzzle_config(config: dict):
    puzzles = {}

    for date, puzzle in config["puzzles"].items():
        puzzles[date.replace("/", "-")] = {
            "board": puzzle["board"],
            "words": decrypt_b64(puzzle["wordScores"]).split(","),
            "bonus_words": decrypt_b64(puzzle["optionalWordScores"]).split(","),
        }

    return puzzles


def write_puzzles(puzzles: dict) -> None:
    for date, puzzel in puzzles.items():
        puzzel_path = pathlib.Path(f"./games/{date}.txt")
        if puzzel_path.exists():
            print(
                f"Skipping puzzle {puzzel_path} as it already exists", file=sys.stderr
            )
        else:
            puzzel_path.write_text("\n".join(puzzel["board"]).upper(), encoding="utf-8")
            print(f"Wrote {puzzel_path} to disk", file=sys.stderr)

        words_path = pathlib.Path(f"./games/{date}_words.txt")
        if words_path.exists():
            print(
                f"Skipping puzzle {words_path} words as it already exists",
                file=sys.stderr,
            )
        else:
            words_path.write_text(
                "\n".join(puzzel["words"] + puzzel["bonus_words"]), encoding="utf-8"
            )
            print(f"Wrote {words_path} to disk", file=sys.stderr)


def main() -> None:
    print(f"Reading current config from {PUZZLE_CONFIG_URL}", file=sys.stderr)
    config = load_puzzle_config()

    print("Parsing loaded config", file=sys.stderr)
    puzzles = parse_puzzle_config(config)

    print("Writing puzzles to ./game directory loaded config", file=sys.stderr)
    write_puzzles(puzzles)


if __name__ == "__main__":
    main()
