# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        accumulator = []
        count = 0
        p_index = 0

        def inorder(node):
            nonlocal count
            nonlocal p_index
            if node:
                inorder(node.left)
                count += 1
                if node is p:
                    p_index = count - 1
                accumulator.append(node)
                inorder(node.right)

        inorder(root)
        if p_index + 1 >= len(accumulator):
            return
        return accumulator[p_index + 1]
