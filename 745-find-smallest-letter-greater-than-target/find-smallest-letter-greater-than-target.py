class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
      l = 0
      r = len(letters)
      
      while l < r:
          mid = (l + r)//2
          
          if letters[mid] <= target:
              l = mid + 1
          else:
              r = mid
              
      return letters[0 if l == len(letters) else l]