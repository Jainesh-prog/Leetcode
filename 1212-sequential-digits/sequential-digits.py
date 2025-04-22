class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        # All sequential digit numbers are substrings of this string
        digits = "123456789"

        # Try all possible lengths of sequential numbers (from 2 to 9 digits)
        for length in range(2, 10):
            # Slide a window of size `length` across "123456789"
            for start in range(0, 10 - length):
                # Extract the substring and convert to integer
                num = int(digits[start:start + length])

                # Only include numbers within the range [low, high]
                if low <= num <= high:
                    result.append(num)

        # Return the result sorted (though it's naturally in order due to input)
        return result
