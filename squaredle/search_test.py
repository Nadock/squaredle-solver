import pathlib

from . import prefix_tree, search, squaredle

_dictionary = [
    w
    for w in pathlib.Path("./words_alpha.txt").read_text("utf-8").split("\n")
    if w and len(w) > 3
]
_dictionary.sort()
prefix = prefix_tree.build_prefix_tree(_dictionary)


def test_find_words__2x2_simple():
    # Arrange
    game = squaredle.load_game("li\nte")
    expected: list[list[str]] = [["lite"], ["itel"], ["tile", "teli", "teil"], []]

    # Act
    actual = search.find_words(game, prefix)

    # Assert
    for expected_words, actual_words in zip(expected, actual, strict=True):
        expected_words.sort()
        actual_words.sort()
        assert expected_words == actual_words


def test_find_words__3x3_real_game():
    # Arrange
    game = squaredle.load_game("LEN\nLIT\nSLY")

    # Act
    found_words = search.find_words(game, prefix)

    # Assert
    for idx, words in enumerate(found_words):
        node = game.nodes[idx]
        for word in words:
            assert word in _dictionary
            assert (
                node.character == word[0]
            ), f"Expected ({idx=}) to start with {node.character}: {word}"
