from typing import List


class Solution:
    def length_of_longest_increasing_subsequence(self, nums: List[int]) -> int:
        n = len(nums)

        cache = {}

        def lis(i, prev):
            if (i, prev) in cache:
                return cache[(i, prev)]
            if i == n:
                return 0
            current = nums[i]
            including = 0
            if prev < current:
                including = 1 + lis(i + 1, current)

            cache[(i, prev)] = max(including, lis(i + 1, prev), lis(i + 1, current))

            return cache[(i, prev)]

        return lis(0, float("-inf"))
