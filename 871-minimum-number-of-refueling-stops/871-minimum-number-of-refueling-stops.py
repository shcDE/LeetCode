from collections import defaultdict

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = defaultdict(int)
        
        dp[0], n = startFuel, len(stations)
        
        for i in range(n):
            position, fuel = stations[i]
            
            for j in range(i, -1, -1):
                if dp[j] >= position:
                    dp[j+1] = max(dp[j+1], dp[j]+fuel)
                    
        for i in range(n+1):
            if dp[i] >= target:
                return i
            
        return -1