# 디스커션 클론함

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, h, o):
            if r < 0 or c < 0 or r == m or c == n:
                return
            
            if val[r][c] & o:
                return
            
            if heights[r][c] < h:
                return
            
            val[r][c] |= o
            if val[r][c] == 3:
                result.append([r, c])
                
            h = heights[r][c]
            dfs(r-1, c, h, o)
            dfs(r+1, c, h, o)
            dfs(r, c-1, h, o)
            dfs(r, c+1, h, o)
            
        m = len(heights)
        n = len(heights[0])
        result = []
        val = [[0]*n for _ in range(m)]
        
        for c in range(n):
            dfs(0, c, 0, 1)
            dfs(m-1, c, 0, 2)
            
        for r in range(m):
            dfs(r, 0, 0, 1)
            dfs(r, n-1, 0, 2)
            
        return result