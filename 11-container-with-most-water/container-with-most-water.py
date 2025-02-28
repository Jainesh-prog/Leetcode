class Solution:
    def maxArea(self, height: List[int]) -> int:
        nums = height
        left, right = 0, len(nums) - 1
        maxx = float("-inf")
        while left < right:
            area = min(nums[left],nums[right])*(right-left)
            maxx = max(area, maxx)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx
