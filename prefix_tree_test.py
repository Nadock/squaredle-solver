import prefix_tree


def test_build_prefix_tree__one_word():
    expected = prefix_tree.PrefixTreeNode.from_dict(
        {
            "prefix": "",
            "children": [
                {
                    "prefix": "h",
                    "children": [
                        {
                            "prefix": "e",
                            "children": [
                                {
                                    "prefix": "l",
                                    "children": [
                                        {
                                            "prefix": "l",
                                            "children": [
                                                {
                                                    "prefix": "o",
                                                    "is_word": True,
                                                }
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
        }
    )

    actual = prefix_tree.build_prefix_tree(["hello"])

    assert actual == expected


def test_build_prefix_tree__two_disjoint_words():
    expected = prefix_tree.PrefixTreeNode.from_dict(
        {
            "prefix": "",
            "children": [
                {
                    "prefix": "h",
                    "children": [
                        {
                            "prefix": "e",
                            "children": [
                                {
                                    "prefix": "l",
                                    "children": [
                                        {
                                            "prefix": "l",
                                            "children": [
                                                {
                                                    "prefix": "o",
                                                    "is_word": True,
                                                }
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
                {
                    "prefix": "w",
                    "children": [
                        {
                            "prefix": "o",
                            "children": [
                                {
                                    "prefix": "r",
                                    "children": [
                                        {
                                            "prefix": "l",
                                            "children": [
                                                {
                                                    "prefix": "d",
                                                    "is_word": True,
                                                }
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
            ],
        }
    )

    actual = prefix_tree.build_prefix_tree(["hello", "world"])

    assert actual == expected


def test_build_prefix_tree__two_overlapping_words():
    expected = prefix_tree.PrefixTreeNode.from_dict(
        {
            "prefix": "",
            "children": [
                {
                    "prefix": "a",
                    "children": [
                        {
                            "prefix": "b",
                            "children": [
                                {
                                    "prefix": "j",
                                    "children": [
                                        {
                                            "prefix": "e",
                                            "children": [
                                                {
                                                    "prefix": "c",
                                                    "children": [
                                                        {
                                                            "prefix": "t",
                                                            "is_word": True,
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "prefix": "u",
                                            "children": [
                                                {
                                                    "prefix": "r",
                                                    "children": [
                                                        {
                                                            "prefix": "e",
                                                            "is_word": True,
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                    ],
                                }
                            ],
                        }
                    ],
                },
            ],
        }
    )

    actual = prefix_tree.build_prefix_tree(["abject", "abjure"])

    assert actual == expected


def test_build_prefix_tree__plurals():
    expected = prefix_tree.PrefixTreeNode.from_dict(
        {
            "prefix": "",
            "children": [
                {
                    "prefix": "w",
                    "children": [
                        {
                            "prefix": "o",
                            "children": [
                                {
                                    "prefix": "r",
                                    "children": [
                                        {
                                            "prefix": "d",
                                            "is_word": True,
                                            "children": [
                                                {
                                                    "prefix": "s",
                                                    "is_word": True,
                                                }
                                            ],
                                        },
                                    ],
                                }
                            ],
                        }
                    ],
                },
            ],
        }
    )

    actual = prefix_tree.build_prefix_tree(["word", "words"])

    assert actual == expected
