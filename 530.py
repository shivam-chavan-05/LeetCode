#Minimum Absolute Difference in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_d = [float('inf')]
        prev = [None]
        def bst(node):
            if not node:
                return
            bst(node.left)
            if prev[0] is not None:
                min_d[0] = min(min_d[0], node.val - prev[0])
            prev[0] = node.val
            bst(node.right)

        bst(root)
        return min_d[0]
