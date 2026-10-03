'''
Day 0
1 attempt
'''
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        counts = Counter(nums)
        top = counts.most_common(1)[0]
        _,max_count = top
        return max_count > 1
        