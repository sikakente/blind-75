from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        O, X = "O", "X"
        temp = "Y"
        rows, cols = len(board), len(board[0])
        boundary_os = {(row, 0) for row in range(rows) if board[row][0] == O}
        boundary_os |= {(row, cols-1)
                        for row in range(rows) if board[row][cols-1] == O}
        boundary_os |= {(0, col) for col in range(cols) if board[0][col] == O}
        boundary_os |= {(rows-1, col)
                        for col in range(cols) if board[rows-1][col] == O}

        def get_neighbors(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            return [(r+x, c+y) for x, y in directions if 0 <= r+x < rows and 0 <= c+y < cols]

        def dfs(r, c, to):
            if board[r][c] == to or board[r][c] == X:
                return
            board[r][c] = to

            for n_r, n_c in get_neighbors(r, c):
                dfs(n_r, n_c, to)

        for row, col in boundary_os:
            dfs(row, col, temp)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == temp:
                    board[row][col] = O
                elif board[row][col] == O:
                    board[row][col] = X


class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        zero_borders = [(r, c) for r in range(rows) for c in range(cols) if (
            r == 0 or c == 0 or r == rows-1 or c == cols-1) and board[r][c] == "O"]

        def get_neighbors(r, c):
            mask = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            return [(r+x, c+y) for x, y in mask if 0 <= r+x < rows and 0 <= c+y < cols]

        def bfs(q):
            while q:
                r, c = q.popleft()
                board[r][c] = "Y"
                for n_r, n_c in get_neighbors(r, c):
                    if board[n_r][n_c] == "O":
                        q.append((n_r, n_c))

        bfs(collections.deque(zero_borders))

        # Tuen existing to X and Y to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Y":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
