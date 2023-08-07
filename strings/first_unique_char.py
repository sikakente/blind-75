from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        checker = Counter(s)

        for i in range(len(s)):
            if checker[s[i]] == 1:
                return i

        return -1
