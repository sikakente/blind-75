from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_checker = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_checker[sorted_s].append(s)

        return anagram_checker.values()
