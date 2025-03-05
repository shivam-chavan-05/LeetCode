#Lowest Common Ancestor of a Binary Search Tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]
        def bst(root):
            if not root:
                return
            lca[0] = root
            if root is p or root is q:
                return
            elif root.val < p.val and root.val < q.val:
                bst(root.right)
            elif root.val > p.val and root.val > q.val:
                bst(root.left)
            else:
                return

        bst(root)
        return lca[0]
