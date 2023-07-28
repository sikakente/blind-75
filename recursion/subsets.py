from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        n = len(nums)

        def helper(index, current_set):
            if index == n:
                sets.append(current_set)
                return

            helper(index+1, current_set + [nums[index]])
            helper(index+1, current_set)
            return

        helper(0, [])
        return sets
