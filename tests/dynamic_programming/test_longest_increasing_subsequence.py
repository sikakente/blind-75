import unittest
import pytest
from dynamic_programming.longest_increasing_subsequence import Solution


@pytest.mark.parametrize("nums,expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1
     )
])
def test_lis(nums, expected):
    assert expected == Solution().length_of_longest_increasing_subsequence(nums)


if __name__ == '__main__':
    unittest.main()
