from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        max_jump = 0
        n = len(nums)
        for i in range(n):
            if max_jump < i:
                return False
            max_jump = max(max_jump, i + nums[i])

        return True
