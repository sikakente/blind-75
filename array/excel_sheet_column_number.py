class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 26

        def get_char_num(char):
            return (ord(char) - ord('A')) + 1

        column_number = 0

        for i in range(len(columnTitle)):
            column_number = (column_number * (base ** i)) + get_char_num(columnTitle[i])

        return column_number
