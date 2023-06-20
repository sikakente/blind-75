class Solution:
    def num_decodings(self, s: str) -> int:
        n = len(s)

        def decode(i):
            if i == n:
                return 1

            if s[i] == "0":
                return 0

            if i == len(s) - 1:
                return 1

            # single digit
            ans = decode(i + 1)
            if int(s[i:i + 2]) <= 26:
                ans += decode(i + 2)

            return ans

        return decode(0)
