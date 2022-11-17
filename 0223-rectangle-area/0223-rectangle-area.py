class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        p = max(ax1, bx1)
        q = max(ay1, by1)
        r = min(ax2, bx2)
        s = min(ay2, by2)
        
        result = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
        
        if p>r or q>s:
            return result
        return result - (p-r)*(q-s)