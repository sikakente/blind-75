class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_negative = n < 0
        if is_negative:
            n = n * -1

        def helper(power):
            if power == 0:
                return 1
            if power == 1:
                return x
            is_even = power % 2 == 0
            half = helper(power//2)
            if is_even:
                return half * half
            return x * half * half

        result = helper(n)
        result = 1/result if is_negative else result

        return round(result, 4)
