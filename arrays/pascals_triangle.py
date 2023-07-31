from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        results = [[1], [1, 1]]

        for i in range(3, numRows+1):
            last_row = results[-1]
            current_row = []
            n_current_row = len(results[-1])
            for j in range(1, n_current_row):
                current_row.append(last_row[j]+last_row[j-1])
            current_row = [1] + current_row + [1]
            results.append(current_row)

        return results
