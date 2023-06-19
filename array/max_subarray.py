from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        max_so_far = float("-inf")
        max_seen = float("-inf")

        for i in range(n):
            max_seen = max(nums[i], max_seen + nums[i])
            max_so_far = max(max_so_far, max_seen)

        return max_so_far
