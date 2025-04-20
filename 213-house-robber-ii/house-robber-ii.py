class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Helper: Run standard DP-based House Robber logic on a subarray
        def rob_range(start, end):
            length = end - start + 1
            if length == 1:
                return nums[start]
            dp = [0] * length
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])

            for i in range(2, length):
                dp[i] = max(dp[i - 1], nums[start + i] + dp[i - 2])

            return dp[-1]

        # Case 1: Rob from index 0 to n - 2 (exclude last)
        max1 = rob_range(0, n - 2)

        # Case 2: Rob from index 1 to n - 1 (exclude first)
        max2 = rob_range(1, n - 1)

        return max(max1, max2)
