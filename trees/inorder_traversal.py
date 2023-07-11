# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        accumulator = []

        def helper(node):
            if node:
                helper(node.left)
                accumulator.append(node.val)
                helper(node.right)

        helper(root)

        return accumulator