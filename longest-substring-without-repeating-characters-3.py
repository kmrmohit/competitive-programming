'''
Day 2
2 attempts, 1wa
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        n = len(s)
        count = {}
        i,j=0,0
        while i<n and j<n:
            currChar = s[j]
            count[currChar] = count.get(currChar, 0) + 1
            while i<j and count[currChar] > 1:
                prevChar = s[i]
                count[prevChar] -= 1
                i += 1
            maxi = max(maxi, j-i+1)
            j+=1
        return maxi