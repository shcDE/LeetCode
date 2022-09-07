# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = ""
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if left or right:
            result += "(%s)" % left
        if right:
            result += "(%s)" % right
        
        return str(root.val) + result