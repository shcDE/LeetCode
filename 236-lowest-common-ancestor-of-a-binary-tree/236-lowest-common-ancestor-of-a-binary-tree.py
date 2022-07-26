# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        def cnt(root, p, q):
            if not root:
                return 0
            
            cur = cnt(root.left, p, q) + cnt(root.right, p, q)
            if root == p or root == q:
                cur += 1
            
            if cur == 2:
                stack.append(root)
            return cur
        
        cnt(root, p, q)
        return stack[0]