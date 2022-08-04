class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        cnt = 1
        while cnt*q%p:
            cnt += 1
            
        if not cnt%2:
            return 2
        return 1 if (cnt * q // p) % 2 else 0