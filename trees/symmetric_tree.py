# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def check_symmetry(left, right):
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            if left is None and right is None:
                return True
            if left.val != right.val:
                return False

            return check_symmetry(left.left, right.right) and check_symmetry(left.right, right.left)

        return root and check_symmetry(root.left, root.right)
