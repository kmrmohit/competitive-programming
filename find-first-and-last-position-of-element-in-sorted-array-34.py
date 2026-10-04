'''
Day 6
1 attempt
'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        def find_lower():
            left, right = 0, n-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    if mid == 0:
                        return mid
                    elif nums[mid-1] == nums[mid]:
                        right = mid-1
                    else:
                        return mid
            return -1

        def find_upper():
            left, right = 0, n-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    if mid == n-1:
                        return mid
                    elif nums[mid+1] == nums[mid]:
                        left = mid+1
                    else:
                        return mid
            return -1
            
        return [find_lower(), find_upper()] 