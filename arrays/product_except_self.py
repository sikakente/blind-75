from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_to_right = [1] * n
        right_to_left = [1] * n

        for i in range(1, n):
            left_to_right[i] = left_to_right[i - 1] * nums[i - 1]

        for i in reversed(range(n - 1)):
            right_to_left[i] = right_to_left[i + 1] * nums[i + 1]

        result = [0] * n

        for i in range(n):
            result[i] = left_to_right[i] * right_to_left[i]

        return result
