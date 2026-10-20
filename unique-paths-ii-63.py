'''
Day 11
1 attempt
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(n) for _ in range(m)]
        dp[0][0] = (obstacleGrid[0][0] ^ 1)
        for i in range(1,n):
            dp[0][i] = (obstacleGrid[0][i] ^ 1) & dp[0][i-1]

        for i in range(1,m):
            dp[i][0] = (obstacleGrid[i][0] ^ 1) & dp[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]