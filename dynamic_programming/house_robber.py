from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        amounts = nums[:]
        max_amount = max(nums[0], nums[1])

        for i in range(2, n):
            amounts[i] = max(amounts[i - 1], nums[i] + amounts[i - 2])
            max_amount = max(amounts[i], max_amount)

        return max_amount



