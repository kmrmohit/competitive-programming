'''
Day 3
2 attempts
'''
class Solution:
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    def is_validpoint(self, i,j,m,n) -> bool:
        return i>=0 and i<m and j>=0 and j<n

    def dfs(self, grid, i, j, m, n):
        if self.is_validpoint(i,j,m,n) and grid[i][j] == '1':
            grid[i][j] = '0'
            self.dfs(grid, i+1, j, m, n) #down
            self.dfs(grid, i, j+1, m, n) #right
            self.dfs(grid, i-1, j, m, n) #up
            self.dfs(grid, i, j-1, m, n) #left
        else:
            return
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '1':
                    islands += 1
                    self.dfs(grid, i,j,m,n)
        return islands