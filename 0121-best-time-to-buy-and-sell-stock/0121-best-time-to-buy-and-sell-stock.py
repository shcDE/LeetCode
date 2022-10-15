class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx, minn = float('inf'), 0
        for p in prices:
    	    if p < maxx: maxx = p
    	    if p - maxx > minn: 
                minn = p - maxx
        return minn