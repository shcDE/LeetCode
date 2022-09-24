# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, sums):
            if not node:
                return
        
            path.append(node.val)
            sums += node.val
            
            if not node.left and not node.right:
                if sums == targetSum:
                    result.append(path.copy())
            else:
                dfs(node.left, path, sums)
                dfs(node.right, path, sums)
                
            path.pop()
            
        result = []
        dfs(root, [], 0)
        
        return result