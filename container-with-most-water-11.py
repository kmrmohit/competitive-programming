'''
Day 1
2 attempts, 1wa
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l,r=0,n-1
        maxi = min(height[0],height[1])
        while l<r:
            maxi = max(maxi, min(height[l],height[r])*(r-l))
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1
        
        return maxi