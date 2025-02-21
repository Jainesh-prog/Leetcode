from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        # **Step 1: Binary Search to Find the Correct Row**
        while top <= bot:
            row = (top + bot) // 2  # Middle row
            if target > matrix[row][-1]:  # Target is larger than last element
                top = row + 1
            elif target < matrix[row][0]:  # Target is smaller than first element
                bot = row - 1
            else:
                break  # The target is within this row

        # If no valid row is found
        if not (top <= bot):
            return False

        # Identify the row where target might be
        row = (top + bot) // 2

        # **Step 2: Binary Search in the Identified Row**
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True  # Target found

        return False  # Target not found
