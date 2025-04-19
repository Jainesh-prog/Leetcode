class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left],height[right])*abs(right-left)
            maxx = max(maxx,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx
            
