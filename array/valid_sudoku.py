from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        size = 9
        rows = [set() for i in range(size)]
        cols = [set() for i in range(size)]
        boxes = [set() for i in range(size)]

        for r in range(size):
            for c in range(size):
                current_value = board[r][c]
                if current_value == ".":
                    continue

                box = (size // 3 * (r // (size // 3))) + (c // (size // 3))
                if current_value in boxes[box] or current_value in rows[r] or current_value in cols[c]:
                    return False
                boxes[box].add(current_value)
                rows[r].add(current_value)
                cols[c].add(current_value)

        return True
