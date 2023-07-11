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


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        cache = {}

        def helper(idx, prev):
            if (idx, prev) in cache:
                return cache[(idx, prev)]
            if idx == n:
                return 0

            including = 0
            if nums[idx] > prev:
                including = 1 + helper(idx + 1, nums[idx])

            excluding = helper(idx + 1, prev)
            cache[(idx, prev)] = max(including, excluding)
            return cache[(idx, prev)]

        return helper(0, float("-inf"))


class Solution3:

    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [0] + nums
        memo = [1 for _ in range(N + 1)]
        memo[0] = 0
        lis = float("-inf")

        for i in range(1, N + 1):
            current_num = nums[i]
            for j in range(1, i):
                compared_num = nums[j]
                if compared_num < current_num and 1 + memo[j] > memo[i]:
                    memo[i] = max(memo[i], 1 + memo[j])

        return max(memo)
