import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [int(tokens[0])]
        operator = {'+', '-', '*', '/'}

        n = len(tokens)
        i = 1
        while stack and i < n:
            current_token = tokens[i]
            if current_token in operator:
                first = stack.pop()
                second = stack.pop()
                result = None
                if current_token == '+':
                    result = second + first
                elif current_token == '-':
                    result = second - first
                elif current_token == '*':
                    result = second * first
                elif current_token == '/':
                    result = second / first
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                if result is not None:
                    stack.append(result)
            else:
                stack.append(int(current_token))
            i += 1
            if i == n:
                break

        return stack[-1]
