from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        right_to_left = [0 for _ in range(n)]
        left_to_right = [0 for _ in range(n)]
        sum_of_heights = 0

        right_to_left[0] = height[0]
        left_to_right[-1] = height[-1]

        for i in range(1, n):
            right_to_left[i] = max(height[i], right_to_left[i-1])

        for i in reversed(range(n-1)):
            left_to_right[i] = max(height[i], left_to_right[i+1])

        for i in range(n):
            sum_of_heights += min(right_to_left[i],
                                  left_to_right[i]) - height[i]
        return sum_of_heights


