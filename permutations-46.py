'''
Day 5
1 attempt
'''
class Solution:
    def solve(self, nums,pos, active):
        n = len(nums)
        if pos == n:
            return []
        result = []
        for (i, num) in enumerate(nums):
            isset = (1<<i) & active
            if not isset:
                subsets = self.solve(nums, pos+1, (1<<i) | active)
                if pos == n-1:
                    return [[num]]
                for sets in subsets:
                    result.append([num] + sets)
        return result
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        return self.solve(nums, 0, 0)