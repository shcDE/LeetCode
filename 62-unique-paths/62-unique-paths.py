class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[True for i in range(n)] for j in range(m)]
        
        dp[0][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
            
        for i in range(1, m):
            dp[i][0] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
        return dp[-1][-1]