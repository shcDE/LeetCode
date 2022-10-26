class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {0:-1}
        
        csum = 0
        
        for i, n in enumerate(nums):
            csum += n
            
            if csum % k in hmap:
                sub_len = i - hmap[csum%k]
                if sub_len > 1:
                    return True
            else:
                hmap[csum%k] = i
                
        return False