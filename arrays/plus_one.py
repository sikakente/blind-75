from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        remainder = 0
        n = len(digits)
        digits[-1] += 1

        for i in reversed(range(n)):
            if remainder:
                digits[i] += 1
            remainder = digits[i] // 10
            if digits[i] == 10:
                digits[i] = digits[i] % 10

        if remainder:
            return [1] + digits
        return digits
