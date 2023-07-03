# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return

        def build(low, high):
            if low > high:
                return
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            node.left = build(low, mid - 1)
            node.right = build(mid + 1, high)

            return node

        return build(0, len(nums) - 1)
