'''
Day 7
1 attempt
'''
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def calc_distance(x: int, y: int) -> int:
            return ((x*x) + (y*y))**0.5
        
        minHeap = [(calc_distance(x,y), [x,y]) for x,y in points]
        heapq.heapify(minHeap)

        output = []
        while k>0:
            _, point = heapq.heappop(minHeap)
            output.append(point)
            k -= 1
        
        return output