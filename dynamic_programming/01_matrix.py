import collections
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        result = [[0 if mat[r][c] == 0 else float(
            "inf") for c in range(cols)] for r in range(rows)]
        zeros = [(r, c) for r in range(rows)
                 for c in range(cols) if mat[r][c] == 0]
        q = collections.deque(zeros)

        def get_neighbors(r, c):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            return [(r+x, c+y) for x, y in directions if 0 <= r+x < rows and 0 <= c+y < cols]

        while q:
            row, col = q.popleft()
            for n_r, n_c in get_neighbors(row, col):
                if mat[n_r][n_c] == 0 or result[n_r][n_c] != float("inf"):
                    continue
                result[n_r][n_c] = result[row][col] + 1
                q.append((n_r, n_c))

        return result
