#!/usr/bin/env python
import pathlib
import sys

from . import prefix_tree, search, squaredle


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

    game_string = game_file.read_text("utf-8").strip()
    words = [w for w in words_file.read_text("utf-8").split("\n") if w and len(w) > 3]
    tree = prefix_tree.build_prefix_tree(words)
    board = squaredle.load_game(game_string)

    print(
        'Loaded Squaredle Game -- "' + game_string.replace("\n", " ") + '"',
        file=sys.stderr,
    )
    print("", file=sys.stderr)

    found_words = search.find_words(board, tree)

    count = 0
    for idx, words in enumerate(found_words):
        count += len(words)
        if words:
            print(
                f"From {board.nodes[idx].character.upper()} ({idx // 3}, {idx % 3}) "
                f"there are {len(words)} words:",
                file=sys.stderr,
            )
            print(", ".join([w.upper() for w in words]))
            print("", file=sys.stderr)

    print(f"Found {count} words in total", file=sys.stderr)


if __name__ == "__main__":
    main()
