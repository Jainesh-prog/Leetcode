class Solution:
    def isPalindrome(self, x: int) -> bool:
        # ❗ Negative numbers and numbers ending with 0 (but not 0 itself) are never palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0  # \U0001f504 This will store the reversed last half of x

        while x > reversed_half:
            # \U0001f525 Take last digit from x and add it to reversed_half
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10  # \U0001f9f9 Remove last digit from x

        # ✅ For even length: x == reversed_half
        # ✅ For odd length: x == reversed_half // 10 (middle digit can be ignored)
        return x == reversed_half or x == reversed_half // 10
