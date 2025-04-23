from bisect import bisect_left
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Step 1: Sort products lexicographically so that suggestions appear in order
        products.sort()

        res = []       # Final result: list of lists of suggestions
        prefix = ""    # Will hold the growing search prefix

        # Step 2: Loop through each character in the search word
        for char in searchWord:
            prefix += char  # Build the prefix one character at a time

            # Step 3: Use binary search to find the first index where prefix could be inserted
            start = bisect_left(products, prefix)

            # Step 4: Check next 3 products (if any) from that index
            suggestions = []
            for i in range(start, min(start + 3, len(products))):
                # Only add product if it actually starts with the current prefix
                if products[i].startswith(prefix):
                    suggestions.append(products[i])

            # Step 5: Append suggestions for this prefix to the final result
            res.append(suggestions)

        # Step 6: Return the complete list of suggestions for each prefix
        return res
