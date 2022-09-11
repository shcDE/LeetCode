import heapq
from math import ceil

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        team = sorted(zip(efficiency, speed), reverse=True)
        pq = []
        MAX = s = 0
        for i in range(n):
            heapq.heappush(pq, team[i][1])
            s += team[i][1]
            if i >= k:
                s -= heapq.heappop(pq)
            MAX = max(MAX, s * team[i][0])
        return MAX % (10**9 + 7)