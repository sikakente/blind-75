import unittest
import pytest
from array.three_sum import Solution


@pytest.mark.parametrize("nums,expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
])
def test_three_sum(nums, expected):
    assert expected == Solution().three_sum(nums)


if __name__ == '__main__':
    unittest.main()
