import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log(n, 4)
        
        if 4**x == 4**int(x):
            return True