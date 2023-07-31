class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parentheses = []

        def generate(closed, opened, s):
            if closed == n and opened == n:
                parentheses.append("".join(s))
                return

            if closed > opened:
                return

            if opened == n:
                generate(closed+1, opened, s + [")"])
                return

            generate(closed, opened+1, s + ["("])
            generate(closed+1, opened, s + [")"])

        generate(0, 0, [])

        return parentheses
