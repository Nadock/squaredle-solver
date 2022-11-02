from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class PrefixTreeNode:
    """
    `PrefixTreeNode` is a single node in a prefix tree.

    `prefix` is the prefix up to this point for the node. For example, in the prefix
    tree representing the word `"hello"` the third node would have a prefix of `"he"`.
    The prefix of the first/root node is always the empty string, ie: `""`.

    `children` is the list of any child nodes from this node which continue to form
    words. For example, in the prefix tree representing the word `"hello"` the third
    node would have one child, the node for the prefix `"hel"`.

    `is_word` indicates if this node in the prefix tree is the last node in a complete
    word. This is always true for leaf nodes but may also be true for nodes that form
    parts of other words, such as compound words or plurals.
    """

    prefix: str
    children: list[PrefixTreeNode] = dataclasses.field(default_factory=list)
    is_word: bool = False

    @classmethod
    def from_dict(cls, d: dict) -> PrefixTreeNode:
        """Build a prefix tree from it's `dict` representation."""
        children = [PrefixTreeNode.from_dict(child) for child in d.pop("children", [])]
        return cls(**d, children=children)

    def to_dict(self) -> dict:
        """
        Return this prefix tree as a `dict` that can be dumped to JSON or reloaded via
        `PrefixTreeNode.from_dict`.
        """
        return dataclasses.asdict(self)

    def add_word(self, word: str, depth: int = 1):
        """
        Add a word to the prefix tree.

        The `depth` parameter should be ignored by callers when operating on the
        root node, which is the recommended way of adding a word to the tree.
        """
        # If we're deeper than the word is long, mark this
        # node as a full word and stop recursing.
        if depth > len(word):
            self.is_word = True
            return

        # Find child node with matching prefix
        prefix = word[:depth]
        matched_node = None
        for child in self.children:
            if child.prefix == prefix:
                matched_node = child

        # Add a new child node if a matching one doesn't exist
        if not matched_node:
            matched_node = PrefixTreeNode(prefix)
            self.children.append(matched_node)

        # Descend recursively until we've built out the tree structure for the entire word
        matched_node.add_word(word, depth + 1)


def build_prefix_tree(words: list[str]) -> PrefixTreeNode:
    """
    Build a single prefix tree from a list of words and return the root node.

    Each supplied word is assumed to be a valid word and will be marked as such in the
    generated prefix tree.
    """
    root = PrefixTreeNode("")

    for word in words:
        root.add_word(word)

    return root
