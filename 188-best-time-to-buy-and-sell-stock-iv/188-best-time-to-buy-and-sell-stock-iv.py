class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k or not prices:
            return 0
        
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        
        for i in range(1, k+1):
            MAX = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(MAX+prices[j], dp[i][j-1])
                MAX = max(MAX, dp[i-1][j] - prices[j])
                
        return dp[-1][-1]