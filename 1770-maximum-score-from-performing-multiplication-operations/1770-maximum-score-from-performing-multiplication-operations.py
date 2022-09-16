class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for l in range(i, -1, -1):
                mul = multipliers[i]
                r = n - 1 - (i - l)
                l_choice = mul*nums[l] + dp[i+1][l+1]
                r_choice = mul*nums[r] + dp[i+1][l]
                dp[i][l] = max(l_choice, r_choice)
          
        return dp[0][0]