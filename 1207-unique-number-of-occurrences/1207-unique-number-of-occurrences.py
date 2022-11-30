import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        values = collections.Counter(arr).values()
        
        return len(set(values)) == len(values)