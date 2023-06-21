"""
# Definition for a Node.
"""
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: 'Node') -> 'Node':
        if node is None:
            return

        queue = collections.deque([node, None])

        clone = {node: Node(node.val)}

        while queue:
            current_node = queue.popleft()
            if current_node:
                for neighbour in current_node.neighbors:
                    if neighbour not in clone:
                        new_node = Node(neighbour.val)
                        clone[neighbour] = new_node
                        queue.append(neighbour)
                        clone[current_node].neighbors.append(new_node)
                    else:
                        clone[current_node].neighbors.append(clone[neighbour])
            else:
                if queue:
                    queue.append(None)

        return clone[node]
