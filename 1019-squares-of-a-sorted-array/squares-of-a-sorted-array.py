class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # \U0001f4e6 Result array initialized with zeros
        left, right = 0, n - 1
        pos = n - 1  # \U0001f9f9 Start filling from the end

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1  # Move to next position from end

        return result
