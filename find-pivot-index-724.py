'''
Day 9
1 attempt
'''
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)
        leftSum = 0
        for index, value in enumerate(nums):
            if totalSum - value == 2*leftSum:
                return index
            leftSum += value
        
        return -1