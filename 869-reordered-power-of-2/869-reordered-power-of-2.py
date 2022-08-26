from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))
        
        for i in range(32):
            if cnt == Counter(str(1<<i)):
                return True
        return False