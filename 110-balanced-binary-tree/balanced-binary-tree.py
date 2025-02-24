# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0  # Base case: return height 0 for None node
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1  # Return -1 to indicate unbalanced tree
            
            return 1 + max(left_depth, right_depth)  # Return height of subtree
        
        return dfs(root) != -1  # If result is -1, tree is unbalanced, otherwise it's balanced
