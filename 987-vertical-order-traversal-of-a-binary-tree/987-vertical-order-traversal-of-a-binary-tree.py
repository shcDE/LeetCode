# 디스커션 클론함

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        tmp = []
        
        def dfs(node, x, y):
            if not node:
                return
            tmp.append((node, x, y))
            dfs(node.left, x-1, y-1)
            dfs(node.right, x+1, y-1)
            
        dfs(root, 0, 0)
        tmp.sort(key=lambda n: (n[1], -n[2], n[0].val))
        
        result = []
        i = 0
        while i < len(tmp):
            subresult = [tmp[i][0].val]
            while i+1 < len(tmp) and tmp[i+1][1] == tmp[i][1]:
                subresult.append(tmp[i+1][0].val)
                i += 1
            result.append(subresult)
            i += 1
        return result