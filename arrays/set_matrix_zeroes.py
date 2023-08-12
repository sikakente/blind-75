class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        FROW, FCOL = False, False

        for val in matrix[0]:
            if val == 0:
                FROW = True
                break
        for row in range(rows):
            if matrix[row][0] == 0:
                FCOL = True

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(1, cols):
                    matrix[row][col] = 0

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0

        if FCOL:
            for row in range(rows):
                matrix[row][0] = 0

        if FROW:
            for col in range(cols):
                matrix[0][col] = 0
