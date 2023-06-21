from collections import defaultdict
from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        in_nodes = defaultdict(int)
        out_nodes = defaultdict(set)
        all_nodes = set()

        for edge in edges:
            from_node, to_node = edge[0], edge[1]
            in_nodes[to_node] += 1
            out_nodes[from_node].add(to_node)
            all_nodes.add(to_node)
            all_nodes.add(from_node)

        zero_nodes = all_nodes - in_nodes.keys()
        nodes_visited = set()

        while zero_nodes:
            zero_in_node = zero_nodes.pop()
            nodes_visited.add(zero_in_node)
            for out_node in out_nodes[zero_in_node]:
                in_nodes[out_node] -= 1
                if in_nodes[out_node] == 0:
                    zero_nodes.add(out_node)

        return len(nodes_visited) == n

# def create_adj_list(n, edges):
#     graph = [set() for _ in range(n)]
#     for edge in edges:
#         u, v = edge[0], edge[1]
#         graph[u].add(v)
#         graph[v].add(u)
#
#     return graph
#
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         WHITE, GREY, BLACK = 0, 1, 2
#         graph = create_adj_list(n, edges)
#
#         def has_cycle(vertex, prev):
#             if visited[vertex] == GREY:
#                 return True
#             visited[vertex] = GREY
#
#             for adj_vertex in graph[vertex]:
#                 if prev == adj_vertex:
#                     continue
#                 if visited[vertex] != BLACK and has_cycle(adj_vertex, vertex):
#                     return True
#
#             visited[vertex] = BLACK
#             return False
#
#         visited = [0] * n
#         if has_cycle(0, -1):
#             return False
#
#         return False if WHITE in visited else True
