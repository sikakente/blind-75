import unittest
import pytest
from graph.pacific_atlantic_water_flow import Solution


@pytest.mark.parametrize("heights,expected", [
    ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
     [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
    ([[1]], [[0, 0]])
])
def test_pacific_atlantic(heights, expected):
    assert expected == Solution().pacific_atlantic(heights)


if __name__ == '__main__':
    unittest.main()
