import unittest
import pytest
from dynamic_programming.coin_change import Solution


@pytest.mark.parametrize("coins,amount,expected", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0)
])
def test_coin_change(coins, amount, expected):
    assert expected == Solution().coin_change(coins, amount)


if __name__ == '__main__':
    unittest.main()
