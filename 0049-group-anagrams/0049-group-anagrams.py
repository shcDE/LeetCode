from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for c in strs:
            dic["".join(sorted(c))].append(c)
            
        return list(dic.values())