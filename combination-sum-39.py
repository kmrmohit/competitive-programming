'''
Day 5
1 attempt
'''
class Solution:
    results = []
    def solve(self, candidates, pos, target, currSet):
        if target == 0:
            self.results.append(currSet)
            return
        if pos >= len(candidates) or target < 0:
            return
        
        num = candidates[pos]
        self.solve(candidates, pos, target - num, [num] + currSet)
        self.solve(candidates, pos+1, target, currSet)
        return

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.results = []
        self.solve(candidates, 0, target, [])
        return self.results
        