from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        visited = set()
        n = len(word)

        def get_neighbors(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            return [(r+x, c+y) for x, y in directions if 0 <= r+x < rows and 0 <= c+y < cols]

        def dfs(r, c, idx):
            if (r, c) in visited:
                return False

            if idx == n:
                return True

            visited.add((r, c))
            for n_r, n_c in get_neighbors(r, c):
                if board[n_r][n_c] == word[idx] and dfs(n_r, n_c, idx+1):
                    return True
            visited.discard((r, c))

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 1):
                        return True

        return False
