class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(number):
            total = 0
            while number:
                number, digit = divmod(number, 10)
                total += digit ** 2
            return total

        slow = n
        fast = sum_squares(n)

        while fast != 1 and fast != slow:
            slow = sum_squares(slow)
            fast = sum_squares(sum_squares(fast))

        if fast == 1:
            return True
        return False
