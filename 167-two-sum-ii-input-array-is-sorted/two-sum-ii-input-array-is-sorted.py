class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        nums = numbers
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return (left+1,right+1)
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return None