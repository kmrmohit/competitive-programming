'''
Day 9
1 attempt
'''
from collections import defaultdict
class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        seatMap = defaultdict(int)
        for booking in bookings:
            [startFlight, lastFlight, seatCount] = booking
            seatMap[startFlight] += seatCount
            seatMap[lastFlight+1] -= seatCount
        
        answer = [0 for i in range(n)]
        currentCount = 0
        for i in range(n):
            currentCount += seatMap[i+1]
            answer[i] = currentCount
        return answer