from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        current_index = 0
        next_non_zero = 1

        while next_non_zero < n:
            if nums[current_index] == 0:
                if nums[next_non_zero] != 0:
                    nums[current_index], nums[next_non_zero] = nums[next_non_zero], nums[current_index]
                    current_index += 1
                    next_non_zero += 1
                else:
                    next_non_zero += 1
            else:
                current_index += 1
                next_non_zero += 1
