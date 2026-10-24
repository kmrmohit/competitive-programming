'''
Day 12
2 attempt
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lenA = len(word1)
        lenB = len(word2)
        dp = [[0] * (lenB+1) for _ in range(lenA+1)]
        # two base cases, when one of the array is empty
        for i in range(1,lenB+1):
            dp[0][i] = 1+dp[0][i-1] # if no characters in A, all in B have to be deleted
        for i in range(1,lenA+1):
            dp[i][0] = 1 + dp[i-1][0] # if no characters in B, all in A have to be deleted
    
        for i in range(1,lenA+1):
            for j in range(1,lenB+1):
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+1 # delete, replace
                dp[i][j] = min(dp[i][j],dp[i][j-1]+1) # insert
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])
        # print(dp)
        return dp[lenA][lenB]