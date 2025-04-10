class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:  # Found target
                return mid
            
            # Check which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target is in left half
                    right = mid - 1
                else:  # Target is in right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target is in right half
                    left = mid + 1
                else:  # Target is in left half
                    right = mid - 1
        
        return -1  # Target not found
