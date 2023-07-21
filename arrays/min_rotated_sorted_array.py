from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        n = len(nums)

        high, low = n - 1, 0

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                high = mid

        return nums[low]
