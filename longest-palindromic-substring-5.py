'''
Day 12
3 attempts
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        dp = [0]*(lens+1)
        maxi = 0
        pos = 0
        for i in range(lens,0,-1):
            tmp = dp.copy()
            for j in range(1, lens+1):
                if s[i-1] == s[j-1]:
                    dp[j] = tmp[j-1] + 1
                else:
                    dp[j] = 0
                if dp[j] > maxi and i==j-dp[j]+1:
                    maxi = dp[j]
                    pos = i-1
        
        return s[pos:maxi+pos]
