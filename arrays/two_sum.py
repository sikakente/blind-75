from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        complement_set = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complement_set:
                return [complement_set[complement], i]

            complement_set[nums[i]] = i

        return []

