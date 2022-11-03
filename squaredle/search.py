from typing import Optional

from . import prefix_tree, squaredle


def find_words(
    game: squaredle.SquaredleGame,
    prefix_root: prefix_tree.PrefixTreeNode,
) -> list[list[str]]:
    """
    Find all the valid words in a Squaredle game.

    Returns a list of lists, one list for each root letter in row-column order. For
    example, the game `"li\nte"` returns list of lists below:

    ```python
    [
        ['lite'],
        ['itel'],
        ['tile', 'teil', 'teli'],
        [],
    ]
    ```
    """
    found_words = []
    all_words: set[str] = set()

    for node in game.nodes:
        new_words = _find_words([], node, prefix_root.get_child(node.character))

        found_words.append(list(new_words.difference(all_words)))
        all_words = all_words.union(new_words)

    return found_words


def _find_words(
    visited: list[squaredle.SquaredleNode],
    node: squaredle.SquaredleNode,
    prefix: Optional[prefix_tree.PrefixTreeNode],
) -> set[str]:

    words: set[str] = set()

    # Stop if we've seen this node before
    if node in visited or not prefix:
        return words
    visited.append(node)

    # If we're at a complete word, add it to the words list
    if prefix.is_word:
        words.add("".join([n.character for n in visited]))

    for edge in node.edges:
        # Continue searching on each edge, if and only if they have a matching prefix
        # tree node and can potentially make a new word.
        edge_prefix = prefix.get_child(edge.character)
        if edge_prefix is not None:
            for word in _find_words(list(visited), edge, edge_prefix):
                words.add(word)

    return words
