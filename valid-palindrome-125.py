'''
Day 1
1 attempt
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while(l<r):
            currLeft,currRight = s[l].lower(),s[r].lower()
            if currLeft.isalnum() and currRight.isalnum() and currLeft == currRight:
                l = l+1
                r = r-1
            elif not currLeft.isalnum():
                l = l+1
            elif not currRight.isalnum():
                r = r-1
            else:
                return False
        return True