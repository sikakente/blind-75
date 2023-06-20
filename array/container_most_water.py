from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n - 1
        area = 0
        while left <= right:
            min_height = min(height[left], height[right])
            width = right - left
            area = max(area, min_height * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return area
