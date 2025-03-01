#Balanced Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height_bal(node):
            if not node:
                return 0

            left = height_bal(node.left)
            if balanced[0] is False:
                return 0
                
            right = height_bal(node.right)

            if abs(left - right) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left, right)

        height_bal(root)
        return balanced[0]
