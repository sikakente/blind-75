import unittest
import pytest
from array.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize("node,expected", [
    (),
    ()
])
def test_clone_graph(node, expected):
    assert expected == Solution().max_profit(node)


if __name__ == '__main__':
    unittest.main()
