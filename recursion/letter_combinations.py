from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        combinations = []
        n = len(digits)
        if n == 0:
            return []
        digit_mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def helper(idx, current_combination):
            if idx == n:
                combinations.append("".join(current_combination))
                return

            for char in digit_mappings[digits[idx]]:
                current_combination.append(char)
                helper(idx + 1, current_combination)
                current_combination.pop()

            return

        helper(0, [])
        return combinations
