import unittest
import pytest
from array.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize("m,n,expected", [
    (),
    ()
])
def test_unique_paths(m,n, expected):
    assert expected == Solution().max_profit(m,n)


if __name__ == '__main__':
    unittest.main()