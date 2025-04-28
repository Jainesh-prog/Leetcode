from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case: sum = 0 has 1 occurrence

        for num in nums:
            curr_sum += num

            # Check if there exists a prefix sum that satisfies the condition
            count += prefix_sum_count[curr_sum - k]

            # Record the current prefix sum
            prefix_sum_count[curr_sum] += 1

        return count
