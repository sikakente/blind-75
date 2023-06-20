import unittest
import pytest
from array.max_product_subarray import Solution


@pytest.mark.parametrize("nums,expected", [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0)
])
def test_max_product_subarray(nums, expected):
    assert expected == Solution().max_product(nums)


if __name__ == '__main__':
    unittest.main()
