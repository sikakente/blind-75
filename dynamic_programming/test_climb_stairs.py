import unittest
import pytest
from dynamic_programming.climbing_stairs import Solution


@pytest.mark.parametrize("n,expected", [
    (2, 2),
    (3, 3)
])
def test_climb_stairs(n, expected):
    assert expected == Solution().climb_stairs(n)


if __name__ == '__main__':
    unittest.main()
