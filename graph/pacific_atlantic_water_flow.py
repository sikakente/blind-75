import collections
from typing import List


class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])

        pacific = [[True if col == 0 or row == 0 else False for col in range(cols)] for row in range(rows)]
        atlantic = [[True if col == cols - 1 or row == rows - 1 else False for col in range(cols)] for row in
                    range(rows)]

        pacific_q = collections.deque([(r, c) for r in range(rows) for c in range(cols) if r == 0 or c == 0])
        atlantic_q = collections.deque(
            [(r, c) for r in range(rows) for c in range(cols) if r == rows - 1 or c == cols - 1])

        def get_neighbors(r, c):
            mask = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            return [(r + x, c + y) for x, y in mask if 0 <= r + x < rows and 0 <= c + y < cols]

        def bfs(q, q_checker):
            while q:
                current_r, current_c = q.popleft()
                for n_r, n_c in get_neighbors(current_r, current_c):
                    if heights[current_r][current_c] <= heights[n_r][n_c] and not q_checker[n_r][n_c]:
                        q.append((n_r, n_c))
                        q_checker[n_r][n_c] = True

        bfs(pacific_q, pacific)
        bfs(atlantic_q, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result
