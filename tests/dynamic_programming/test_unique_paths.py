import unittest
import pytest
from dynamic_programming.unique_paths import Solution


@pytest.mark.parametrize("m,n,expected", [
    (3, 7, 28),
    (3, 2, 3)
])
def test_unique_paths(m, n, expected):
    assert expected == Solution().unique_paths(m, n)


if __name__ == '__main__':
    unittest.main()
