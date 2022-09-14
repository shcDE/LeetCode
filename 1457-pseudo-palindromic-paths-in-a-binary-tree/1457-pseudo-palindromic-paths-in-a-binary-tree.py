# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        result = []
        
        def dfs(node, path):
            if not node:
                return node
            
            path ^= 2**node.val
            
            if not node.left and not node.right and path&(path-1) == 0:
                result.append(path)
            else:
                dfs(node.left, path)
                dfs(node.right, path)
                
        dfs(root, 0)
        
        return len(result)