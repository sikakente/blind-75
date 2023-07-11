class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        base = 26
        needle_len = len(needle)

        def rolling_hash(text):
            text_hash = 0
            for i in range(len(text)):
                text_hash = (text_hash * base) + ord(text[i])
            return text_hash

        haystack_hash = rolling_hash(haystack[:needle_len])
        needle_hash = rolling_hash(needle)
        power_needle = base ** max(needle_len - 1, 0)

        for i in range(needle_len, len(haystack)):
            if haystack_hash == needle_hash and needle == haystack[i - needle_len:i]:
                return i - needle_len
            haystack_hash -= ord(haystack[i - needle_len]) * power_needle
            haystack_hash = (haystack_hash * base) + ord(haystack[i])

        if haystack_hash == needle_hash and haystack[-needle_len:] == needle:
            return len(haystack) - needle_len

        return -1
