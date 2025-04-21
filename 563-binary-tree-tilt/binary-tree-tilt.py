class Solution:
  def findTilt(self, root: Optional[TreeNode]) -> int:
      self.tilt = 0
      
      def dfs(node):
          if node == None:
              return 0
          
          l = dfs(node.left)
          r = dfs(node.right)
          
          self.tilt += abs(l - r)
          return l + r + node.val
          
      dfs(root)
      return self.tilt