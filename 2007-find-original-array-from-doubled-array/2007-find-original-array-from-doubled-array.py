from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnts = Counter(changed)
        result = []
        
        for i in sorted(changed):
            if cnts[i] > 0 and cnts[i*2] > 0:
                cnts[i] -= 1
                
                if i == 0:
                    if cnts[i] > 0:
                        cnts[i] -= 1
                        result.append(i)
                
                else:
                    cnts[i*2] -= 1
                    result.append(i)
        
        return result if len(result) * 2 == len(changed) else []