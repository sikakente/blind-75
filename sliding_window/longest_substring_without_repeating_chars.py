import collections


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        n = len(s)
        char_checker = collections.defaultdict(int)

        right, left = 0, 0
        longest_substring = 0

        while right < n:
            current_char = s[right]
            char_checker[current_char] += 1
            right += 1

            while char_checker[current_char] > 1 and left <= right:
                char_checker[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left)

        return longest_substring
