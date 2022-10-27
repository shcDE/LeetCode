#디스커션 클론함

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        def shifted_overlap(img1, img2, r_shift, c_shift):
            n = len(img1)
            overlap = 0
            for row in range(max(0, -r_shift), min(n-r_shift, n)):
                for col in range(max(-c_shift, 0), min(n-c_shift, n)):
                    if img1[row+r_shift][col+c_shift] == 1 and img2[row][col] == 1:
                        overlap += 1
            
            return overlap
        
        output = 0
        
        for r_shift in range(-n, n+1):
            for c_shift in range(-n, n+1):
                overlap = shifted_overlap(img1, img2, r_shift, c_shift)
                output = max(overlap, output)
                
        return output