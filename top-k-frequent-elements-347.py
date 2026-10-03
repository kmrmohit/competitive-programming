'''
Day 0
1 attempt
'''
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        output = []
        while k > 0:
            topno, topcount = counts.most_common()[0]
            output.append(topno)
            print(topno,topcount)
            k = k-1
            counts[topno] = 0
        return output