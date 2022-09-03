class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))
        
        dp = [[[] for _ in range(10)] for _ in range(n)]
        
        dp[0] = [[i] for i in range(10)]
        for i in range(1, n):
            for j in range(10):
                for K in set([j-k, j+k]):
                    if not 0 <= K < 10:
                        continue
                    for N in dp[i-1][K]:
                        dp[i][j].append(j*10**i+N)
                        
        result = []
        
        for i in range(1, 10):
            for j in dp[n-1][i]:
                result.append(j)
                
        return result