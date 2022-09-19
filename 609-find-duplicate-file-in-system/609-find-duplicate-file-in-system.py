from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        if not paths:
            return paths
        
        ct_map = defaultdict(list)
        
        for p in paths:
            sp = p.split()
            dic_name = sp[0]
            
            for i in range(1, len(sp)):
                ct = sp[i].split('(', 1)[1].split(')')[0]
                file_name = sp[i].partition('(')[0]
                
                ct_map[ct].append(dic_name + "/" + file_name)
                
        candidates = []
        
        for key, value in ct_map.items():
            if len(value) > 1:
                candidates.append(value)
                
        return candidates