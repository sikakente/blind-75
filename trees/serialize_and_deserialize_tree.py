# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
from trees.utils.tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        q = collections.deque([root])
        serialized_tree = []

        while q:
            current = q.popleft()
            if current is None:
                serialized_tree.append('None')
                continue
            serialized_tree.append(f"{current.val}")
            left = current.left or None
            right = current.right or None
            q.append(left)
            q.append(right)
        
        while serialized_tree:
          last_item = serialized_tree[-1]
          if last_item != 'None':
              break
          serialized_tree.pop()

        return ','.join(serialized_tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return

        data = data.split(',')
        root = TreeNode(data[0])
        q = collections.deque([root])
        i = 1

        while q and i < len(data):
            current_node = q.popleft()
            if current_node == None:
                i += 1
                continue
            if data[i] != 'None':
                left_node = TreeNode(data[i])
                current_node.left = left_node
                q.append(left_node)
            i += 1
            if data[i] != 'None':
                right_node = TreeNode(data[i])
                current_node.right = right_node
                q.append(right_node)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
