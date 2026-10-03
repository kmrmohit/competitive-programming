'''
Day 1
3 attempts, 1wa,1tle
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        resultSet = []
        nums = sorted(nums)
        uniques = {}
        n = len(nums)

        for i in range(0, n):
            j, k = i+1, n-1
            while j<k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == 0:
                    key = tuple(sorted([nums[i],nums[j],nums[k]]))
                    if not uniques.get(key):
                        resultSet.append([nums[i],nums[j],nums[k]])
                        uniques[key] = 1
                    if nums[k] == nums[i]:
                        break
                    j = j+1
                elif currSum < 0:
                    j = j+1
                else:
                    k = k-1
        return resultSet