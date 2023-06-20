class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        cache = {}

        def common_subsequence(p1, p2):
            if (p1, p2) in cache:
                return cache[(p1, p2)]
            if p1 == n:
                return 0
            if p2 == m:
                return 0

            including = 0
            if text1[p1] == text2[p2]:
                including = 1 + common_subsequence(p1 + 1, p2 + 1)

            cache[(p1, p2)] = max(including, common_subsequence(p1 + 1, p2), common_subsequence(p1, p2 + 1))
            return cache[(p1, p2)]

        return common_subsequence(0, 0)