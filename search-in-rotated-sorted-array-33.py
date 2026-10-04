'''
Day 6
1 attempt
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        
        def find_pivot(nums):
            left,right=0,n-1
            while left<=right:
                mid = (left+right)//2
                # consider right > mid > left
                if nums[right] >= nums[mid] and nums[mid] >= nums[left]:
                    # check if we are in rotated section
                    if nums[mid] <= nums[n-1]:
                        right = mid-1 # if we are in rotated section, we need to move left
                    else:
                        left = mid+1 # else we need to move right
                # consider mid > right and mid >= left, meaning we are in left section
                elif nums[mid] >= nums[left] and nums[mid] > nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            return left
        
        pivot = find_pivot(nums)

        def find_element(leftLimit, rightLimit):
            while leftLimit <= rightLimit:
                mid = (leftLimit + rightLimit)//2
                if nums[mid] ==target:
                    return mid
                elif nums[mid] > target:
                    rightLimit = mid-1
                else:
                    leftLimit = mid+1
            return -1

        leftLimit, rightLimit = 0, n-1
        if target >= nums[pivot] and target <= nums[n-1]:
            leftLimit = pivot
        else:
            rightLimit = pivot-1
        
        return find_element(leftLimit, rightLimit)