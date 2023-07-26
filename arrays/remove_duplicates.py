from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        prev_index, next_index, = 0, 1

        while next_index < len(nums):
            if nums[next_index] == nums[prev_index]:
                del nums[next_index]
            else:
                next_index += 1
                prev_index += 1

        return len(nums)
