import collections
from typing import List

WATER, LAND = "0", "1"


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        is_visited = [[False for _ in range(cols)] for _ in range(rows)]

        def get_neighbors(r, c):
            mask = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            return [(r + x, c + y) for x, y in mask if 0 <= r + x < rows and 0 <= c + y < cols]

        def dfs(r, c):
            if is_visited[r][c]:
                return
            is_visited[r][c] = True

            for neighbor_r, neighbor_c in get_neighbors(r, c):
                if grid[neighbor_r][neighbor_c] == LAND:
                    dfs(neighbor_r, neighbor_c)

        island_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == LAND and not is_visited[row][col]:
                    dfs(row, col)
                    island_count += 1

        return island_count


class Solution2:
    # faster version using bfs
    def numIslands(self, grid: List[List[str]]) -> int:

        LAND, WATER = "1", "0"

        rows, cols = len(grid), len(grid[0])
        is_visited = [[False for _ in range(cols)] for _ in range(rows)]

        def get_neighbors(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            return [(r+x, c+y) for x, y in directions if 0 <= r+x < rows and 0 <= c+y < cols]

        def bfs(r, c):
            q = collections.deque([(r, c)])

            while q:
                current_r, current_c = q.popleft()
                if is_visited[current_r][current_c]:
                    continue
                is_visited[current_r][current_c] = True
                for n_r, n_c in get_neighbors(current_r, current_c):
                    if grid[n_r][n_c] == LAND:
                        q.append((n_r, n_c))

        island_count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == LAND and not is_visited[row][col]:
                    bfs(row, col)
                    island_count += 1

        return island_count
