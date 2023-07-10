from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        n_row = len(matrix)
        n_col = len(matrix[0])
        count = 0

        def go_right(left, right, row):
            nonlocal count
            for i in range(left, min(right + 1, n_col)):
                order.append(matrix[row][i])
                count += 1

        def go_down(top, bottom, col):
            nonlocal count
            for i in range(top, min(bottom + 1, n_row)):
                order.append(matrix[i][col])
                count += 1

        def go_left(left, right, row):
            nonlocal count
            for i in reversed(range(left, min(right + 1, n_col))):
                order.append(matrix[row][i])
                count += 1

        def go_up(top, bottom, col):
            nonlocal count
            for i in reversed(range(top, min(bottom + 1, n_row))):
                order.append(matrix[i][col])
                count += 1

        n = len(matrix) * len(matrix[0])

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while count < n:
            go_right(left, right, top)
            top += 1
            if count == n:
                break
            go_down(top, bottom, right)
            right -= 1
            if count == n:
                break
            go_left(left, right, bottom)
            bottom -= 1
            if count == n:
                break
            go_up(top, bottom, left)
            left += 1
            if count == n:
                break

        return order
