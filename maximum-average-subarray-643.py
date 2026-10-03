'''
Day 2
1 attempt
'''
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxi = None
        currSum = 0
        for i in range(0,len(nums)):
            currSum = currSum + nums[i]
            if i >= k:
                currSum -= nums[i-k]
            if i >= k-1:
                maxi = currSum/k if maxi is None else max(maxi, currSum/k)
        return maxi
                