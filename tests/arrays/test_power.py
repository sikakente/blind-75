import pytest
from arrays.power import Solution


@pytest.mark.parametrize('x,n,expected', [
    (2.00000, 10, 1024.00000),
    (2.10000, 3, 9.26100),
    (2.0000, -2, 0.25000)
])
def test_power(x, n, expected):
    assert expected == Solution().myPow(x, n)
