import unittest
import pytest
from dynamic_programming.combination_sum import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([1, 2, 3], 4, 7),
    ([9], 3, 0)
])
def test_combination_sum(nums, target, expected):
    assert expected == Solution().combination_sum4(nums, target)


if __name__ == '__main__':
    unittest.main()
