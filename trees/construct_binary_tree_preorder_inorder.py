# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        current_idx = 0

        def build(inorder_list):
            nonlocal current_idx
            if current_idx > n:
                return
            if current_idx == n:
                return

            current_val = preorder[current_idx]
            node = TreeNode(current_val)
            inorder_n = len(inorder_list)
            inorder_index = 0
            for i in range(inorder_n):
                if current_val == inorder_list[i]:
                    inorder_index = i
                    break
            left_side = inorder_list[:inorder_index]
            if left_side:
                current_idx += 1
                node.left = build(left_side)

            right_side = inorder_list[inorder_index+1:]
            if right_side:
                current_idx += 1
                node.right = build(right_side)

            return node

        return build(inorder)
