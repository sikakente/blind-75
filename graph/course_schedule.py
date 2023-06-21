from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        # in_nodes
        in_nodes = defaultdict(set)
        out_nodes = defaultdict(set)
        all_courses = set()
        for p in prerequisites:
            course, prereq = p[0], p[1]
            in_nodes[prereq].add(course)
            out_nodes[course].add(prereq)
            all_courses.add(course)
            all_courses.add(prereq)

        zero_nodes = all_courses - set(in_nodes.keys())
        done = set()

        while zero_nodes:
            node = zero_nodes.pop()
            for out_node in out_nodes[node]:
                in_nodes[out_node].remove(node)
                if len(in_nodes[out_node]) == 0:
                    zero_nodes.add(out_node)
            done.add(node)

        return len(done) == len(all_courses)

        # out_nodes
        # zero_in_nodes
        #

        # WHITE, GREY, BLACK = 0, 1, 2
        # visited = [WHITE for _ in range(numCourses)]
        # def build_graph():
        #     graph = [set() for _ in range(numCourses)]

        #     for p in prerequisites:
        #         course, prereq = p[0], p[1]
        #         graph[prereq].add(course)

        #     return graph

        # def has_cycle(course, graph):
        #     if visited[course] == GREY:
        #         return True
        #     visited[course] = GREY
        #     for next_course in graph[course]:
        #         if visited[next_course] != BLACK and has_cycle(next_course, graph):
        #             return True
        #     visited[course] = BLACK
        #     return False

        # graph = build_graph()
        # for c in range(numCourses):
        #     if visited[c] == WHITE and has_cycle(c, graph):
        #         return False

        # return True
