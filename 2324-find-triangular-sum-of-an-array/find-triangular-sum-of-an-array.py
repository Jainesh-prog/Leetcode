class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Keep reducing the array until one element remains
        while len(nums) > 1:
            # Replace nums with the adjacent pairwise sum % 10
            nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
        return nums[0]

