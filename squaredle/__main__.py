#!/usr/bin/env python
import pathlib
import sys

from . import prefix_tree


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: squaredle.py [words_file]", file=sys.stderr)
        sys.exit(1)

    words_file = pathlib.Path(sys.argv[1])
    if not words_file.is_file():
        print(f"Expected regular file at {words_file}", file=sys.stderr)
        sys.exit(1)

    words = words_file.read_text("utf-8").split("\n")
    print(f"Loaded {len(words)} from {words_file}", file=sys.stderr)

    tree = prefix_tree.build_prefix_tree(words)
    print(f"Built prefix tree from {len(words)} words", file=sys.stderr)


if __name__ == "__main__":
    main()
