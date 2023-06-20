from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 1:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, n):
            temp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            max_so_far = temp_max
            result = max(result, max_so_far)
        return result
