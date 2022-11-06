class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        else:
            find = set()
            while s not in find:
                find.add(s)
                s = s[k:] + s[:k]
                
            return min(find)