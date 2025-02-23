#invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        #Post Order Traversal
        def invert(node):
            if not node:
                return 
            invert(node.left)
            invert(node.right)            
            node.left, node.right = node.right, node.left

        invert(root)
        return root
