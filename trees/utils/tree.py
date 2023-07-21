import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"<Node={self.val}>"


def deserialize_tree(elements: List[int]) -> TreeNode:
    n = len(elements)

    def helper(idx):
        if idx >= n:
            return

        if elements[idx] is None:
            return

        node = TreeNode(elements[idx])
        left_index = (2 * idx) + 1
        right_index = (2 * idx) + 2

        node.left = helper(left_index)
        node.right = helper(right_index)

        return node

    root = helper(0)
    return root


def serialize_tree(root: TreeNode):
    serialized_tree = []
    q = collections.deque([root])

    while q:
        current = q.popleft()
        if current:
            serialized_tree.append(current.val)
            if current.left:
                q.append(current.left)
            else:
                q.append(None)

            if current.right:
                q.append(current.right)
            else:
                q.append(None)
        else:
            if q:
                serialized_tree.append(None)

    while serialized_tree:
        last_element = serialized_tree[-1]
        if last_element:
            break
        serialized_tree.pop()

    return serialized_tree


def inorder(root):
    traversal = []

    def helper(node):
        if node:
            helper(node.left)
            traversal.append(node.val)
            helper(node.right)

    helper(root)
    return traversal
