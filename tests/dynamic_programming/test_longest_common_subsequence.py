import unittest
import pytest
from dynamic_programming.longest_common_subsequence import Solution


@pytest.mark.parametrize("text1,text2,expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0)
])
def test_longest_common_subsequence(text1, text2, expected):
    assert expected == Solution().longest_common_subsequence(text1, text2)


if __name__ == '__main__':
    unittest.main()
