from __future__ import annotations

import dataclasses
from typing import Iterator, Optional, Tuple


@dataclasses.dataclass
class SquaredleNode:
    character: str
    edges: list[SquaredleNode] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class SquaredleGame:
    size: int
    nodes: list[SquaredleNode]

    def __post_init__(self):
        self.link_nodes()

    def get(self, row: int, col: int) -> Optional[SquaredleNode]:
        """
        Retrieve the node at the specified (`row`, `col`) position, or `None` if the
        position is outside the grid.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.nodes[(row * self.size) + col]
        return None

    def iter_grid(self) -> Iterator[Tuple[int, int, SquaredleNode]]:
        """Iterate through the grid of nodes yielding `(row, col, node)` each time."""
        for row in range(self.size):
            for col in range(self.size):
                node = self.get(row, col)
                if node is None:
                    raise ValueError(f"Expected valid node at ({row}, {col})")
                yield row, col, node

    def link_nodes(self) -> None:
        """Update each game node's links, should be called if the board is modified."""
        for row, col, node in self.iter_grid():
            for row_offset in [-1, 0, 1]:
                for col_offset in [-1, 0, 1]:
                    if row_offset == col_offset == 0:
                        continue
                    edge_node = self.get(row + row_offset, col + col_offset)
                    if edge_node:
                        node.edges.append(edge_node)


def load_game(game: str) -> SquaredleGame:
    """
    Load a Squaredle game from it's string representation.

    The game string is a top-left to bottom-right and newline separated sequence of
    characters in the Squaredle puzzle. For example, the following puzzle has the
    string representation `"LEN\nLIT\nSLY"`:

    ```
    L E N
    L I T
    S L Y
    ```

    Squaredle games are "square" (duh) so each line in the game string must have the
    same number of characters as there are lines.
    """
    lines = game.lower().split("\n")
    size = len(lines)
    nodes = []

    for idx, line in enumerate(lines):
        if len(line) != len(lines):
            raise ValueError(
                f"Expected line {idx+1} to be {len(lines)} characters long, "
                f"got {len(line)} characters instead"
            )

        for char in line:
            nodes.append(SquaredleNode(char))

    return SquaredleGame(size, nodes)
