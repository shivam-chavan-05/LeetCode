# Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)
            h = left + right
            if max_d[0] < h:
                max_d[0] = h
            return 1 + max(left, right)
        
        height(root)
        return max_d[0]
