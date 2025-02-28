from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count_map = Counter(nums)  # Optimized counting

        # Step 2: Use heap to get k most frequent elements
        return [num for num, _ in heapq.nlargest(k, count_map.items(), key=lambda item: item[1])]
