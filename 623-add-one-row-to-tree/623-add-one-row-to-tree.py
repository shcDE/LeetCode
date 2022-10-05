# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root is None:
            if depth == 1:
                root = TreeNode(val)
            return root
        
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        
        if depth == 2:
            left, right = root.left, root.right
            new_left, new_right = TreeNode(val), TreeNode(val)
            new_left.left, new_right.right = left, right
            root.left, root.right = new_left, new_right
            return root
        
        left = self.addOneRow(root.left, val, depth-1)
        right = self.addOneRow(root.right, val, depth-1)
        
        root.left, root.right = left, right
        
        return root