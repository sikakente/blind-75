import pytest
from arrays.search_rotated_sorted_array import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1)
])
def test_search(nums, target, expected):
    assert expected == Solution().search(nums, target)
