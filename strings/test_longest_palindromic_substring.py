import unittest
import pytest
from array.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize("s,expected", [
    (),
    ()
])
def test_longest_palindrome(s, expected):
    assert expected == Solution().max_profit(s)


if __name__ == '__main__':
    unittest.main()
