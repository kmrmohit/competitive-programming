'''
Day 1
1 attempt
'''
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r=0,len(numbers)-1
        while l<r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l+1,r+1]
            elif currSum < target:
                l = l+1
            else:
                r = r-1