class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        onestep = 1
        twostep = 2
        
        for i in range(n-2):
            onestep, twostep = twostep, onestep + twostep
        
        return twostep