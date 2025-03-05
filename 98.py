#Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [float('-inf')]
        isValid = [True]
        def bst(node):
            if not node:
                return
            
            bst(node.left)
            if node.val > prev[0]:
                prev[0] = node.val
                bst(node.right)
            else:
                isValid[0] = False

        bst(root)
        return isValid[0]
