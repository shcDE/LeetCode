#디스커션 참고함
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        result = 0
        cum_p = 0
        
        for g, p in sorted(zip(growTime, plantTime), reverse = True):
            cum_p += p
            result = max(result, cum_p + g)
            
        return result