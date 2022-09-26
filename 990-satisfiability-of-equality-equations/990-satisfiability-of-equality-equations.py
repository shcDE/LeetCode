class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(n):
            n = ord(n) - ord('a')
            while root[n] != n:
                n = root[n]
                
            return n
        
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            root[r2] = r1
            
        root = list(range(26))
        
        for e in equations:
            if e[1] == '=':
                union(e[0], e[-1])
                
        for e in equations:
            if e[1] == '!' and find(e[0]) == find(e[-1]):
                return False
            
        return True