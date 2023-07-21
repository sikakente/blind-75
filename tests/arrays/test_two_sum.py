import pytest
from arrays.two_sum import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2])
])
def test_two_sum(nums, target, expected):
    assert expected == Solution().two_sum(nums, target)
