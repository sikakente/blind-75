from typing import List


class Solution:
    def word_break(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def find(s):
            if s == '':
                return True
            if s in memo:
                return memo[s]

            for word in wordDict:
                # current word is at beginning of string
                if s.find(word) == 0:
                    # strip the remaining of the word
                    rem = s[len(word):]
                    if find(rem):
                        memo[rem] = True
                        return True

            memo[s] = False
            return memo[s]

        return find(s)
