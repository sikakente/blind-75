from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        checker = set()
        for num in nums:
            if num in checker:
                return True
            checker.add(num)

        return False
