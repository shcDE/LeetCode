class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        m ,n = len(grid)-1, len(grid[0])-1
        def dfs(i, j):
            if i > m or i < 0 or j < 0 or j > n or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        isLands = 0
        for i in range(m+1):
            for j in range(n+1):
                if grid[i][j] == '1':
                    isLands += 1
                    dfs(i, j)
        return isLands