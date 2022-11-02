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
                            "prefix": "he",
                            "children": [
                                {
                                    "prefix": "hel",
                                    "children": [
                                        {
                                            "prefix": "hell",
                                            "children": [
                                                {
                                                    "prefix": "hello",
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
                            "prefix": "he",
                            "children": [
                                {
                                    "prefix": "hel",
                                    "children": [
                                        {
                                            "prefix": "hell",
                                            "children": [
                                                {
                                                    "prefix": "hello",
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
                            "prefix": "wo",
                            "children": [
                                {
                                    "prefix": "wor",
                                    "children": [
                                        {
                                            "prefix": "worl",
                                            "children": [
                                                {
                                                    "prefix": "world",
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
                            "prefix": "ab",
                            "children": [
                                {
                                    "prefix": "abj",
                                    "children": [
                                        {
                                            "prefix": "abje",
                                            "children": [
                                                {
                                                    "prefix": "abjec",
                                                    "children": [
                                                        {
                                                            "prefix": "abject",
                                                            "is_word": True,
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "prefix": "abju",
                                            "children": [
                                                {
                                                    "prefix": "abjur",
                                                    "children": [
                                                        {
                                                            "prefix": "abjure",
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
                            "prefix": "wo",
                            "children": [
                                {
                                    "prefix": "wor",
                                    "children": [
                                        {
                                            "prefix": "word",
                                            "is_word": True,
                                            "children": [
                                                {
                                                    "prefix": "words",
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
