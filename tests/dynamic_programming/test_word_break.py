import unittest
import pytest
from dynamic_programming.word_break import Solution


@pytest.mark.parametrize("s,word_dict,expected", [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)
])
def test_word_break(s, word_dict, expected):
    assert expected == Solution().word_break(s, word_dict)


if __name__ == '__main__':
    unittest.main()
