class Solution:
    def findCelebrity(self, n: int) -> int:
        if n <= 0:
            return -1
        if n == 1:
            return 0

        stack = [i for i in range(n)]

        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()

            if knows(a, b):
                stack.append(b)
            else:
                stack.append(a)

        c = stack.pop()

        for i in range(n):
            if (i != c and knows(c, i) or not knows(i, c)):
                return -1

        return c
