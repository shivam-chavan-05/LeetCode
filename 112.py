# Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sumPath(node, curSum):
            if not node:
                return False
            
            curSum += node.val

            if not node.left and not node.right:
                return curSum == targetSum

            return (sumPath(node.left, curSum) or sumPath(node.right, curSum))
            
        return sumPath(root, 0)
