import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all non-alphanumeric characters and convert to lowercase
        words = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Use two pointers to check palindrome
        first = 0
        last = len(words) - 1
        
        while first < last:
            if words[first] != words[last]:
                return False
            first += 1
            last -= 1
        
        return True
