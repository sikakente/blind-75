import unittest
import pytest
from arrays.container_most_water import Solution


@pytest.mark.parametrize("height,expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
])
def test_test_max_area(height, expected):
    assert expected == Solution().max_area(height)


if __name__ == '__main__':
    unittest.main()
