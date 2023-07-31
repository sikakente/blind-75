import collections


class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        if is_negative:
            x = x * -1

        digits = collections.deque([])
        exp = 1
        num_digits = 0
        reverse = 0

        while x:
            x, end_number = divmod(x, 10)
            reverse = (reverse * 10) + end_number

        reverse = reverse * -1 if is_negative else reverse
        upper, lower = (2 ** 31) - 1, -(2 ** 31)
        return reverse if lower <= reverse <= upper else 0
