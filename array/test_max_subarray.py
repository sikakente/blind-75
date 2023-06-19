import unittest
import pytest
from array.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize("nums,expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23)
])
def test_max_subarray(nums, expected):
    assert expected == Solution().max_profit(nums)


if __name__ == '__main__':
    unittest.main()
