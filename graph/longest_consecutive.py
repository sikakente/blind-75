from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size == 0:
            return 0
        if nums_size == 1:
            return 1

        num_checker = {num: False for num in nums}
        max_window_size = 0

        nums_to_visit = len(num_checker.keys())
        nums_seen = 0

        for num, used in num_checker.items():
            if used:
                continue
            current_window_size = 1
            num_checker[num] = True
            nums_seen += 1
            # check numbers above
            next_num = num + 1
            while next_num in num_checker:
                num_checker[next_num] = True
                next_num += 1
                current_window_size += 1
                nums_seen += 1

            # check numbers below
            next_num = num - 1
            while next_num in num_checker:
                num_checker[next_num] = True
                next_num -= 1
                current_window_size += 1
                nums_seen += 1

            max_window_size = max(current_window_size, max_window_size)
            if nums_seen == nums_to_visit:
                break

        return max_window_size
