import pytest
from trees.utils.tree import serialize_tree, deserialize_tree


@pytest.mark.parametrize('serialized, expected', [
    ([-10, 9, 20, None, None, 15, 7], [-10, 9, 20, None, None, 15, 7])
    ([1, 2, 3], [1, 2, 3])
])
def test_deserialize_and_serialize_tree(serialized, expected):
    root = deserialize_tree(serialized)
    assert root.val == expected[0]

    assert expected == serialize_tree(root)
