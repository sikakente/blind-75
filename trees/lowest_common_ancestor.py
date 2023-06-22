from collections import namedtuple

Ancestor = namedtuple("Ancestor", "num_nodes ancestor")


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node is None:
                return Ancestor(num_nodes=0, ancestor=None)

            left_val = helper(node.left)
            if left_val.num_nodes == 2 and left_val.ancestor is not None:
                return left_val

            right_val = helper(node.right)
            if right_val.num_nodes == 2 and right_val.ancestor is not None:
                return right_val

            num_nodes = (left_val.num_nodes + right_val.num_nodes + (p, q).count(node))
            return Ancestor(num_nodes=2, ancestor=node) if num_nodes == 2 else Ancestor(num_nodes=num_nodes,
                                                                                        ancestor=None)

        ans = helper(root)
        return ans.ancestor
