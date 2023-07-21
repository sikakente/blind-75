import unittest
import pytest
from dynamic_programming.house_robber import Solution


@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12)
])
def test_rob(nums, expected):
    assert expected == Solution().rob(nums)


if __name__ == '__main__':
    unittest.main()
