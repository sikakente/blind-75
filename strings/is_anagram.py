from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_checker = Counter(s)

        for t_char in t:
            if t_char in s_checker and s_checker[t_char] > 0:
                s_checker[t_char] -= 1
            else:
                return False
        return True
