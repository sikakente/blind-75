import pytest
from dynamic_programming.trapping_rain_water import Solution


@pytest.mark.parametrize('height,expected', [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9)
])
def test_trapping_rain_water(height, expected):
    assert expected == Solution().trap(height)
