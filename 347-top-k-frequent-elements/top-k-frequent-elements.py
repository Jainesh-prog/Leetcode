from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number using a hashmap
        count = {}  # {num: frequency}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Create buckets where index = frequency
        # Each bucket[i] will contain all numbers that appear i times
        freq = [[] for i in range(len(nums) + 1)]  # max possible freq is len(nums)
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: Traverse buckets in reverse (from highest freq to lowest)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # Stop when we’ve collected top k frequent elements
                if len(res) == k:
                    return res
