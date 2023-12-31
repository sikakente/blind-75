class Solution:
    def num_decodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def decode(i):
            if i in memo:
                return memo[i]

            if i == n:
                return 1

            if s[i] == "0":
                return 0

            if i == len(s) - 1:
                return 1

            # single digit
            ans = decode(i + 1)
            
            # double digit must be between 1 and 26
            if int(s[i:i + 2]) <= 26:
                ans += decode(i + 2)

            memo[i] = ans
            return ans

        return decode(0)
