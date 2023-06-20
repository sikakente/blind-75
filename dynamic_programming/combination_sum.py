from typing import List


class Solution:
    def combination_sum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        cache = {}

        def helper(remaining):
            if remaining in cache:
                return cache[remaining]
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            comb_sum = 0
            for i in range(n):
                if nums[i] <= remaining:
                    comb_sum += helper(remaining - nums[i])

            cache[remaining] = comb_sum
            return cache[remaining]

        return helper(target)
