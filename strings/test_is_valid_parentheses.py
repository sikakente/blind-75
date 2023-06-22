import unittest
import pytest
from strings.is_valid_parentheses import Solution


@pytest.mark.parametrize("s,expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False)
])
def test_is_valid_parentheses(s, expected):
    assert expected == Solution().is_valid(s)


if __name__ == '__main__':
    unittest.main()
