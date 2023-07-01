from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n + m == 0:
            return
        if n + m == 1:
            if nums1:
                return nums1[0]
            return nums2[0]

        def merge():
            merged_list = [None] * (n + m)
            i, j, k = 0, 0, 0

            while i < n and j < m:
                if nums1[i] <= nums2[j]:
                    merged_list[k] = nums1[i]
                    i += 1
                else:
                    merged_list[k] = nums2[j]
                    j += 1
                k += 1

            while i < n:
                merged_list[k] = nums1[i]
                i += 1
                k += 1

            while j < m:
                merged_list[k] = nums2[j]
                j += 1
                k += 1

            return merged_list

        def get_median(merged_list):
            merged_list_size = len(merged_list)
            is_even = merged_list_size % 2 == 0
            middle_index = merged_list_size // 2
            if is_even:
                return (merged_list[middle_index - 1] + merged_list[middle_index]) / 2

            return merged_list[middle_index]

        return get_median(merge())
