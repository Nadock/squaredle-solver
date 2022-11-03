import pytest

from . import squaredle


@pytest.mark.parametrize(
    "game,valid", [("", False), ("AB\nCD", True), ("AB\nC", False)]
)
def test_load_game__line_length_check(game: str, valid: bool):
    if valid:
        assert squaredle.load_game(game)
    else:
        with pytest.raises(ValueError):
            squaredle.load_game(game)


def test_load_game__3x3_correct_nodes():
    # Arrange
    expected_nodes = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    # Act
    board = squaredle.load_game("ABC\nDEF\nGHI")

    # Assert
    for idx, node in enumerate(board.nodes):
        assert node.character == expected_nodes[idx]


def test_load_game__3x3_correct_links():
    # Arrange
    expected_edges = [
        ["b", "d", "e"],
        ["a", "c", "d", "e", "f"],
        ["b", "e", "f"],
        ["a", "b", "e", "g", "h"],
        ["a", "b", "c", "d", "f", "g", "h", "i"],
        ["b", "c", "e", "h", "i"],
        ["d", "e", "h"],
        ["d", "e", "f", "g", "i"],
        ["e", "f", "h"],
    ]

    # Act
    board = squaredle.load_game("ABC\nDEF\nGHI")

    # Assert
    for idx, node in enumerate(board.nodes):
        actual_edges = [node.character for node in node.edges]
        actual_edges.sort()
        assert expected_edges[idx] == actual_edges
