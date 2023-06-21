from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        is_visited = [False] * n
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(vertex):
            if is_visited[vertex]:
                return
            is_visited[vertex] = True

            for adjacent_vertex in graph[vertex]:
                dfs(adjacent_vertex)

        count = 0
        for i in range(n):
            if not is_visited[i]:
                dfs(i)
                count += 1

        return count
