import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"<Node={self.val}>"

    def __repr__(self) -> str:
        return f"<Node={self.val}>"


def deserialize_tree(data: List[int]) -> TreeNode:
    if data == []:
        return

    root = TreeNode(data[0])
    q = collections.deque([root])
    i = 1

    while q and i < len(data):
        current_node = q.popleft()
        if current_node == None:
            i += 1
            continue
        if data[i] is not None:
            left_node = TreeNode(data[i])
            current_node.left = left_node
            q.append(left_node)
        i += 1
        if data[i] is not None:
            right_node = TreeNode(data[i])
            current_node.right = right_node
            q.append(right_node)
        i += 1

    return root


def serialize_tree(root: TreeNode):
    if root is None:
        return []
    q = collections.deque([root])
    serialized_tree = []

    while q:
        current = q.popleft()
        if current is None:
            serialized_tree.append(None)
            continue
        serialized_tree.append(current.val)
        q.append(current.left)
        q.append(current.right)

    while serialized_tree:
        last_item = serialized_tree[-1]
        if last_item is not None:
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


def preorder(root):
    traversal = []

    def helper(node):
        if node:
            traversal.append(node.val)
            helper(node.left)
            helper(node.right)
    helper(root)
    return traversal


def postorder(root):
    traversal = []

    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            traversal.append(node.val)
    helper(root)
    return traversal
