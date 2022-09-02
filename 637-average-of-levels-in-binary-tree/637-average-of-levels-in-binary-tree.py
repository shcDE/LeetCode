# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop()
            levels[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        result = []
        
        for level in levels.values():
            result.append(sum(level)/len(level))
            
        return result