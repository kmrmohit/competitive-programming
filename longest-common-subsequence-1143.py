'''
Day 12
2 attempt
Notes
1. how to copy a list - list(org), org.copy(),org[:], works for shallow lists
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1len = len(text1)
        text2len = len(text2)
        if text1len > text2len:
            text1,text2=text2,text1
            text1len,text2len=text2len,text1len
        lcsdp = [0] * (text1len+1)
        for i in range(1, text2len+1):
            tempdp = list(lcsdp)
            for j in range(1,text1len+1):
                lcsdp[j] = max(lcsdp[j-1],tempdp[j])
                if text1[j-1] == text2[i-1]:
                    lcsdp[j] = max(tempdp[j-1]+1,lcsdp[j])
        return lcsdp[text1len]