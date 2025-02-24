# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # Global variable to track the max diameter

        def dfs(node):
            if not node:
                return 0  # Base case: return 0 if the node is None
            
            left_depth = dfs(node.left)  # Compute left subtree depth
            right_depth = dfs(node.right)  # Compute right subtree depth

            # Update max diameter if the current node’s left + right path is greater
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1  # Return height of this node

        dfs(root)
        return self.max_diameter
        