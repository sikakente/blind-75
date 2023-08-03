from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for row in range(n//2):
            for col in range(row, n-row-1):
                matrix[row][col], matrix[col][n-1 -
                                              row] = matrix[col][n-1-row], matrix[row][col]
                matrix[row][col], matrix[n-1-row][n-1 -
                                                  col] = matrix[n-1-row][n-1-col], matrix[row][col]
                matrix[row][col], matrix[n-1-col][row] = matrix[n -
                                                                1-col][row], matrix[row][col]
