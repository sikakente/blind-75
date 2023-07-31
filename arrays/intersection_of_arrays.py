import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_freq = collections.Counter(nums1)
        intersection = []

        for num in nums2:
            if num in nums1_freq and nums1_freq[num] > 0:
                intersection.append(num)
                nums1_freq[num] -= 1
        
        return intersection