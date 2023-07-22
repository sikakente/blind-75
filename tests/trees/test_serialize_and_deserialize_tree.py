
import pytest
from trees.serialize_and_deserialize_tree import Codec


@pytest.mark.parametrize('tree,expected', [
    ('1,2,3,None,None,4,5', '1,2,3,None,None,4,5')
])
def test_serialize_and_deserialize_tree(tree, expected):
    ser = Codec()
    deser = Codec()
    assert ser.serialize(deser.deserialize(tree)) == expected
