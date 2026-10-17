'''
Day 9
1 attempt
'''
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        storeSumCount = defaultdict(int)
        storeSumCount[0] = 1
        prefixSum = 0
        total = 0
        for value in nums:
            prefixSum += value
            diff = prefixSum - k
            total += storeSumCount[diff]
            storeSumCount[prefixSum] += 1
        
        return total
