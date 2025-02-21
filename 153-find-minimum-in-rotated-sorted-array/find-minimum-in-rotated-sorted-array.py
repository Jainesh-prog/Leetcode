from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:  # No need for `<=` because `left == right` gives the min
            mid = (left + right) // 2
            
            # Check for the pivot (minimum element)
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # Binary Search Decision
            if nums[mid] > nums[right]:  # Pivot is in the right half
                left = mid + 1
            else:  # Pivot is in the left half
                right = mid
        
        return nums[left]  # `left` will always point to the smallest element
