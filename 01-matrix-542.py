'''
Day 4
1 attempt
'''
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        from collections import deque
        que = deque()
        m,n=len(mat),len(mat[0])
        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j]==0:
                    que.append((i,j,2))
                else:
                    mat[i][j] = -1
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while que:
            (i,j,t) = que.popleft()
            for dir in directions:
                [dx,dy]=dir
                nx,ny=i+dx,j+dy
                if nx>=0 and nx<m and ny>=0 and ny<n and mat[nx][ny]==-1:
                    mat[nx][ny] = t+1
                    que.append((nx,ny,t+1))
        
        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j]>=2:
                    mat[i][j] -= 2
        return mat