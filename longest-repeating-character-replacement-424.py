'''
Day 2
2 attempts, 1wa
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        n = len(s)
        for i in range(0,26):
            left,right,converted,currMax=0,0,0,0
            while left<=right and right<n:
                currChar = ord(s[right]) - 65 # ascii for 'A' is 65
                if currChar == i:
                    right += 1
                elif converted < k:
                    converted += 1
                    right += 1
                else:
                    if k>0:
                        while converted == k:
                            prevChar = ord(s[left]) - 65
                            if prevChar != i:
                                converted -= 1
                            left += 1
                    else:
                        right = right + 1
                        left = right
                currMax = max(currMax, right-left)
            maxi = max(maxi, currMax)
        return maxi