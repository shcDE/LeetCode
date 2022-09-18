class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        l_max = height[l]
        r_max = height[r]
        
        result = 0
        
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                result += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                result += r_max - height[r]
                
        return result