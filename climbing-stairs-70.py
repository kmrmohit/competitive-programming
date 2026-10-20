'''
Day 11
1 attempts
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        noOfWays: list = [0 for i in range(n+1)]
        noOfWays[0] = noOfWays[1] = 1
        for i in range(2,n+1):
            noOfWays[i] = noOfWays[i-2] + noOfWays[i-1]

        return noOfWays[n]