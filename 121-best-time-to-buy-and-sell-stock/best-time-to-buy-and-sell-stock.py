class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = float('inf')

        for price in prices:
            mini = min(mini, price)
            profit = max(profit, price - mini)

        return profit
        