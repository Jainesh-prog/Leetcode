class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left+right)//2
            sum = 0
            for element in nums:
                sum += math.ceil(element/mid)
            if sum <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
