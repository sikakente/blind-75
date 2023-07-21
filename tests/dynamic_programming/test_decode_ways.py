import unittest
import pytest
from dynamic_programming.decode_ways import Solution


@pytest.mark.parametrize("s,expected", [
    ("12", 2),
    ("226", 3),
    ("06", 0)
])
def test_decode_ways(s, expected):
    assert expected == Solution().num_decodings(s)


if __name__ == '__main__':
    unittest.main()
