class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        if not matrix or not matrix[0]:
            return res

        # Dimensions of the matrix
        m, n = len(matrix), len(matrix[0])

        # Direction: 0 = →, 1 = ↓, 2 = ←, 3 = ↑
        direction = 0

        # Boundaries to keep track of spiral layers
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            if direction == 0:
                # Traverse from left to right across the top row
                for j in range(left, right + 1):
                    res.append(matrix[top][j])
                top += 1  # Move top boundary down
            elif direction == 1:
                # Traverse from top to bottom along the right column
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1  # Move right boundary left
            elif direction == 2:
                # Traverse from right to left across the bottom row
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1  # Move bottom boundary up
            elif direction == 3:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # Move left boundary right

            # Move to next direction
            direction = (direction + 1) % 4

        return res
