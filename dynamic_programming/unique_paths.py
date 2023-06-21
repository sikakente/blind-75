class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        cache = {}

        def paths(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0

            cache[(i, j)] = paths(i + 1, j) + paths(i, j + 1)
            return cache[(i, j)]

        return paths(0, 0)
