# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        kth_smallest = None

        def inorder(node):
            nonlocal counter
            nonlocal kth_smallest
            if node:
                inorder(node.left)
                counter -= 1
                if counter == 0:
                    kth_smallest = node.val
                    return
                inorder(node.right)

        inorder(root)
        return kth_smallest
