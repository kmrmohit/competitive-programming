'''
Day 2
1 attempt
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        miniLength = n+1
        i,j=0,0
        currSum = 0
        while i<=j and j<n:
            currSum += nums[j]
            while i<j and currSum - nums[i] >= target:
                currSum -= nums[i]
                i += 1
            # print(i,j,currSum)
            miniLength = miniLength if currSum < target else min(miniLength, j-i+1)
            j += 1
        return miniLength if miniLength != n+1 else 0