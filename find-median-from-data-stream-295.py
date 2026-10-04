'''
Day 7
3 attempts
'''
import heapq

class MedianFinder:
    def __init__(self):
        self.minH,self.maxH = [],[]

    def addNum(self, num: int) -> None:
        sizeMinh = len(self.minH)
        sizeMaxh = len(self.maxH)
        if sizeMaxh == 0:
            heapq.heappush(self.maxH, (-num, num))
        elif sizeMinh == 0:
            heapq.heappush(self.minH, (num, num))
            if num < self.maxH[0][1]:
                self.minH[0],self.maxH[0] = (-self.maxH[0][0], self.maxH[0][1]), (-self.minH[0][0],self.minH[0][1])
        else:
            if sizeMaxh <= sizeMinh:
                if num <= self.maxH[0][1]:
                    heapq.heappush(self.maxH, (-num,num))
                else:
                    heapq.heappush(self.minH, (num, num))
                    (priority, val) = heapq.heappop(self.minH)
                    heapq.heappush(self.maxH, (-priority, val))
            else:
                if num >= self.minH[0][1]:
                    heapq.heappush(self.minH, (num,num))
                else:
                    heapq.heappush(self.maxH, (-num,num))
                    (priority, val) = heapq.heappop(self.maxH)
                    heapq.heappush(self.minH, (-priority, val))
    

    def findMedian(self) -> float:
        sizeMinh = len(self.minH)
        sizeMaxh = len(self.maxH)
        # print(self.maxH, self.minH)
        if sizeMinh == sizeMaxh:
            return (self.minH[0][1] + self.maxH[0][1])/2
        return self.maxH[0][1] if sizeMinh < sizeMaxh else self.minH[0][1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()