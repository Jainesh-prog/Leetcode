from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the max, min products as the first element, and overall max as well.
        max_product = min_product = result = nums[0]
        
        for i in range(1, len(nums)):
            current = nums[i]
            # Swap max_product and min_product if current is negative
            if current < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product
            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)
            
            # Update the result with the maximum product found so far
            result = max(result, max_product)
        
        return result
