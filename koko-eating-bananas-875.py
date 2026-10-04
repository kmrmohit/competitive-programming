'''
Day 6
1 attempt
'''
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)

        def ceildivison(a,b) -> int:
            return -(-a // b)

        mini, maxi = 1, max(piles)
        while mini <= maxi:
            mid = (mini+maxi) // 2
            turn_time = sum(ceildivison(pile, mid) for pile in piles)
            if turn_time <= h:
                maxi = mid-1
            else:
                mini = mid+1

        return maxi+1