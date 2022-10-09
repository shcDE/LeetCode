# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        queue, sets = [root], set()
        while queue:
            level = []
            for node in queue:
                if k - node.val in sets:
                    return True
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                sets.add(node.val)
            queue = level
        return False