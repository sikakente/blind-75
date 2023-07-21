import unittest
import pytest
from sliding_window.longest_substring_without_repeating_chars import Solution


@pytest.mark.parametrize("s,expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
])
def test_longest_substring_without_repeating(s, expected):
    assert expected == Solution().length_of_longest_substring(s)


if __name__ == '__main__':
    unittest.main()
