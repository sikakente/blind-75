from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        partition = []
        n = len(s)

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        def helper(idx):
            if idx == n:
                result.append(partition[:])
                return

            for j in range(idx, n):
                if is_palindrome(idx, j):
                    partition.append(s[idx:j+1])
                    helper(j+1)
                    partition.pop()

        helper(0)
        return result
