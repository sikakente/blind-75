import pytest
from arrays.min_rotated_sorted_array import Solution


@pytest.mark.parametrize("nums,expected", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11)
])
def test_find_min(nums, expected):
    assert expected == Solution().find_min(nums)
