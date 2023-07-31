class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        lo, hi = 0, x

        while lo < hi:
            mid = (lo+hi) / 2
            possible_root = mid * mid
            if x - 0.00005 <= possible_root <= x + 0.00005:
                return int(mid)
            elif possible_root < x:
                lo = mid
            else:
                hi = mid

        return 0
