from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def helper(node):
            nonlocal max_sum
            if node is None:
                return 0

            left_path_sum = helper(node.left)
            right_path_sum = helper(node.right)

            current_node_path_sum = max(node.val, node.val + (max(left_path_sum, right_path_sum)))
            max_sum = max(max_sum, current_node_path_sum, node.val + left_path_sum + right_path_sum)
            return current_node_path_sum

        helper(root)
        return max_sum
