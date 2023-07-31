from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        END = '*'
        cols, rows = len(board[0]), len(board)
        found = set()
        visited = set()

        def insertInTrie(word):
            current = trie
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current[END] = True

        def get_neighbors(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            return [(r+x, c+y) for x, y in directions if 0 <= r+x < rows and 0 <= c+y < cols]

        def dfs(r, c, current_trie, current_word):
            if (r, c) in visited:
                return
            if END in current_trie:
                found.add("".join(current_word))

            visited.add((r, c))
            for n_r, n_c in get_neighbors(r, c):
                if board[n_r][n_c] in current_trie:
                    dfs(n_r, n_c, current_trie[board[n_r][n_c]],
                        current_word + [board[n_r][n_c]])
            visited.discard((r, c))

        for word in words:
            insertInTrie(word)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    dfs(row, col, trie[board[row][col]], [board[row][col]])

        return list(found)
