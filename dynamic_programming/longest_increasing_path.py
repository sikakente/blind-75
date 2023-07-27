from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def get_neighbor(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            return [(r+x, c+y) for x, y in directions if 0 <= r+x < rows and 0 <= c+y < cols]

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            current_val = matrix[r][c]

            max_path_length = 1
            for n_r, n_c in get_neighbor(r, c):
                if current_val < matrix[n_r][n_c]:
                    max_path_length = max(max_path_length, 1 + dfs(n_r, n_c))

            memo[(r, c)] = max_path_length

            return max_path_length

        longest_path = 0
        for row in range(rows):
            for col in range(cols):
                longest_path = max(dfs(row, col), longest_path)

        return longest_path
