class Solution:
    def longest_palindrome(self, s: str) -> str:
        n = len(s)

        def palindrome_starting_from(left, right):
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            return [left, right]

        max_palindrome = [0, 0]

        for i in range(n):
            odd_palindrome = palindrome_starting_from(i, i)
            even_palindrome = palindrome_starting_from(i - 1, i)
            max_between_odd_even = max(odd_palindrome, even_palindrome, key=lambda x: x[1] - x[0])
            max_palindrome = max(max_between_odd_even, max_palindrome, key=lambda x: x[1] - x[0])

        return max_palindrome
