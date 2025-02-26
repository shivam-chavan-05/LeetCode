# Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_subtree(node1, node2):
            if not node1 and not node2:
                return True
            
            if (node1 and not node2) or (not node1 and node2):
                return False
            
            if node1.val != node2.val:
                return False

            return is_subtree(node1.left, node2.left) and is_subtree(node1.right, node2.right)

        def has_subtree(node):
            if not node:
                return False
            
            if is_subtree(node, subRoot):
                return True

            return has_subtree(node.left) or has_subtree(node.right)

        return has_subtree(root)
