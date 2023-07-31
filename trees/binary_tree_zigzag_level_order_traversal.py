# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        all_levels = []
        q = collections.deque([root, None])
        current_level = collections.deque([])
        reverse = False

        while q:
            current = q.popleft()
            if current:
                if reverse:
                    current_level.appendleft(current.val)
                elif not reverse:
                    current_level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            else:
                if q:
                    q.append(None)
                all_levels.append(current_level)
                current_level = collections.deque([])
                reverse = not reverse

        return all_levels
