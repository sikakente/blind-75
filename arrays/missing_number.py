from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        n = len(nums)
        actual = sum(nums)
        expected_sum = (n * (n + 1)) // 2

        if expected_sum != actual:
            return expected_sum - actual
        return -1
