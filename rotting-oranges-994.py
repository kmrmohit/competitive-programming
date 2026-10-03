'''
Day 4
2 attempts
'''
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        que = deque()
        m = len(grid)
        n = len(grid[0])
        countFresh = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 2:
                    que.append((i,j,0))
                elif grid[i][j] == 1:
                    grid[i][j] = -1
                    countFresh += 1
        
        ans = 0
        while que:
            (i,j,t) = que.popleft()
            ans = max(ans, t)
            for point in dir:
                [dx,dy]=point
                nx = i+dx
                ny = j+dy
                if nx>=0 and nx<m and ny>=0 and ny<n and grid[nx][ny]==-1:
                    countFresh -= 1
                    grid[nx][ny] = t+1
                    que.append((nx,ny,t+1))
        return ans if countFresh == 0 else -1