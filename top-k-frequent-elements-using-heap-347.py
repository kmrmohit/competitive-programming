'''
Day 7
1 attempt
'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        import heapq
        maxHeap = [(-frequency, num) for num, frequency in counts.items()]
        output = []
        heapq.heapify(maxHeap)
        while k>0:
            kthfreqVal, kthfreqNum = heapq.heappop(maxHeap)
            output.append(kthfreqNum)
            k -= 1
        return output