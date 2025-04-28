from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()

        # \U0001f9f9 Step 1: Initialize distances and queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))  # Add all 0s to the queue
                else:
                    mat[r][c] = -1  # Mark unvisited 1s

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 directions

        # \U0001f501 Step 2: BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds and if neighbor not visited yet
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1  # Update distance
                    queue.append((nr, nc))  # Add neighbor to queue

        return mat
