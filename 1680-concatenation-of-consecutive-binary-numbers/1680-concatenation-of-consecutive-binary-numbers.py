class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = ['{0:b}'.format(i) for i in range(1, n+1)]
        
        return int(''.join(result), 2)%(10**9+7)