class Solution:
    def romanToInt(self, s: str) -> int:
        prev_char = None
        int_value = 0

        symbol_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n = len(s)

        for i in reversed(range(n)):
            current_val = symbol_map[s[i]]
            if prev_char:
                previous_num = symbol_map[prev_char]
                if previous_num > current_val:
                    int_value -= current_val
                else:
                    int_value += current_val
            else:
                int_value += current_val
            prev_char = s[i]

        return int_value

    def romanToInt2(self, s: str) -> int:
        char_map = {
            'I': {'value': 1, 'less': set()},
            'V': {'value': 5, 'less': {'I'}},
            'X': {'value': 10, 'less': {'I', 'V'}},
            'L': {'value': 50, 'less': {'I', 'V', 'X'}},
            'C': {'value': 100, 'less': {'I', 'V', 'X', 'L'}},
            'D': {'value': 500, 'less': {'I', 'V', 'X', 'L', 'C'}},
            'M': {'value': 1000, 'less': {'I', 'V', 'X', 'L', 'C', 'D'}}
        }

        if len(s) <= 1:
            return char_map[s].get('value', 0)
        int_val = char_map[s[0]].get('value', 0)
        for i in range(1, len(s)):
            current_char = char_map[s[i]]
            if s[i-1] in current_char['less']:
                int_val -= 2 * char_map[s[i-1]]['value']
            int_val += current_char['value']

        return int_val
