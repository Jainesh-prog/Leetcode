class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Step 1: Create DP array
        dp = [0] * n

        # Step 2: Base cases
        dp[0] = nums[0]               # If only one house, rob it
        dp[1] = max(nums[0], nums[1]) # Max of robbing first or second house

        # Step 3: Fill the DP array
        for i in range(2, n):
            # Either rob current + dp[i-2], or skip current and take dp[i-1]
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        # Step 4: Return max amount from last house
        return dp[-1]
