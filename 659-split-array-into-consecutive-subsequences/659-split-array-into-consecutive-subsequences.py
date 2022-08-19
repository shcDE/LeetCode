from collections import defaultdict
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        lens = defaultdict(list)
        
        for n in nums:
            length = 1
            if len(lens[n - 1]) > 0:
                length += heapq.heappop(lens[n - 1])
            heapq.heappush(lens[n], length)
        
        for len_arr in lens.values():
            if len_arr and min(len_arr) < 3: 
                return False           
        return True