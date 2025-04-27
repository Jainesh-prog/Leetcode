from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # \U0001f4e6 Separate even and odd indexed elements
        even = nums[::2]
        odd = nums[1::2]

        # \U0001f9ee Count frequencies for both groups
        even_count = Counter(even)
        odd_count = Counter(odd)

        # \U0001f3c6 Find top 2 most common elements in even and odd positions
        even_top = even_count.most_common(2)  # List of (element, frequency)
        odd_top = odd_count.most_common(2)

        # \U0001f6e1️ Helper: fetch top element's count safely (0 if missing)
        def get_count(top_list, idx):
            return top_list[idx][1] if idx < len(top_list) else 0

        # ✏️ Option 1: most frequent even != most frequent odd
        if even_top and odd_top and even_top[0][0] != odd_top[0][0]:
            return n - (even_top[0][1] + odd_top[0][1])
        
        # ✏️ Option 2: most frequent even == most frequent odd
        # Need to pick second-best for either even or odd to avoid same values

        # Two scenarios:
        change_even = get_count(even_top, 1) + get_count(odd_top, 0)  # even uses 2nd best
        change_odd = get_count(even_top, 0) + get_count(odd_top, 1)   # odd uses 2nd best

        # Pick the one that requires fewer changes
        return n - max(change_even, change_odd)
