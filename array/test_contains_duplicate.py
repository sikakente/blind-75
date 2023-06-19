import unittest
import pytest
from array.contains_duplicate import Solution


@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False)
])
def test_contains_duplicate(nums, expected):
    assert expected == Solution().contains_duplicate(nums)


if __name__ == '__main__':
    unittest.main()
