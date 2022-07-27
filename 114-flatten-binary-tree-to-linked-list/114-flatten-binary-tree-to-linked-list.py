# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def find(root):
            if not root:
                return None, None
            lhead, ltail = find(root.left)
            rhead, rtail = find(root.right)
            root.right, root.left = lhead if lhead else rhead, None
            if ltail:
                ltail.right = rhead
            return root, rtail if rtail else (ltail if ltail else root)
        
        find(root)