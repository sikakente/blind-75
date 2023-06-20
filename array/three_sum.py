from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 2:
            return []

        nums.sort()
        triplets = set()

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                if triplet_sum == 0:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    left += 1

        return [list(triplet) for triplet in triplets]
