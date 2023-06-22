class Solution:
    def is_valid(self, s: str) -> bool:
        complement = {"}": "{", "]": "[", ")": "("}
        stack = []
        for char in s:
            if char not in complement:
                stack.append(char)
            else:
                if stack:
                    if stack.pop() != complement[char]:
                        return False
                else:
                    return False

        return False if stack else True
