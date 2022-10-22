class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generator(l, r, ps, result = []):
            if l:
                generator(l-1, r, ps+ '(')
            if l < r:
                generator(l, r-1, ps+ ")")
            if len(ps) == 2*n:
                result.append(ps)
            
            return result
        
        return generator(n, n, "")