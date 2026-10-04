'''
Day 7
1 attempt
'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        import heapq
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int|None:
        if len(self.nums) < self.k - 1:
            heapq.heappush(self.nums, val)
            return None
        elif len(self.nums) == self.k - 1:
            heapq.heappush(self.nums, val)
        else:
            if val > self.nums[0]:
                heapq.heapreplace(self.nums, val)
        # print(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)