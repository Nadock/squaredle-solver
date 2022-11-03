#!/usr/bin/env python
import pathlib
import sys

from . import prefix_tree, squaredle


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: squaredle.py [words_file] [game_file]", file=sys.stderr)
        sys.exit(1)

    words_file = pathlib.Path(sys.argv[1])
    if not words_file.is_file():
        print(f"Expected regular file at {words_file}", file=sys.stderr)
        sys.exit(1)

    game_file = pathlib.Path(sys.argv[2])
    if not game_file.is_file():
        print(f"Expected regular file at {game_file}", file=sys.stderr)
        sys.exit(1)
    game_string = game_file.read_text().strip()

    words = words_file.read_text("utf-8").split("\n")
    print(f"Loaded {len(words)} from {words_file}", file=sys.stderr)

    tree = prefix_tree.build_prefix_tree(words)
    print(f"Built prefix tree from {len(words)} words", file=sys.stderr)

    board = squaredle.load_game(game_string)
    print("Loaded game board for " + game_string.replace("\n", "\\n"), file=sys.stderr)


if __name__ == "__main__":
    main()
