import unittest
import pytest
from dynamic_programming.can_jump import Solution


@pytest.mark.parametrize("nums,expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
def test_can_jump(nums, expected):
    assert expected == Solution().can_jump(nums)


if __name__ == '__main__':
    unittest.main()
