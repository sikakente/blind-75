from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if target == nums[0] else -1

        high, low = n - 1, 0
        min_index = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > high:
                low = mid + 1
            elif nums[mid] <= high:
                high = mid

        def binary_search(lo, hi):

            while lo <= hi:
                m = (lo + hi) // 2
                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    lo = m + 1
                else:
                    hi = m - 1
            return -1

        # low -> end, beg -> low
        min_index = low

        if target <= nums[n - 1]:
            return binary_search(min_index, n - 1)

        return binary_search(0, min_index - 1)
