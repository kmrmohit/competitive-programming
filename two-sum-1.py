'''
Day 0
1 attempt
'''
from collections import Counter

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        counts = Counter(nums)
        numA, numB = None, None
        for (index,num) in enumerate(nums):
            rem = target - num
            if rem == num and counts[rem] >= 2:
                numA = index
                numB = rem
                break
            elif rem!=num and counts[rem] > 0:
                numA = index
                numB = rem
                break
        print (numA,numB)
        for (index,num) in enumerate(nums):
            if num==numB and index!=numA:
                return [numA, index]