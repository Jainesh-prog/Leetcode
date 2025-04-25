class Solution:
    def letterCombinations(self, digits):
        # \U0001f4cc Base case: If input is empty, return empty list
        if not digits:
            return []

        # \U0001f4de Mapping of digits to letters like on a phone keypad
        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        # \U0001f4dd Final result list to collect all valid combinations
        res = []

        # \U0001f9e0 Backtracking function
        def backtrack(index, path):
            # ✅ If we've built a complete combination
            if index == len(digits):
                res.append("".join(path))
                return

            # \U0001f501 Get possible letters for current digit
            letters = phone[digits[index]]

            # \U0001f503 Try each letter and recurse
            for letter in letters:
                path.append(letter)          # Choose
                backtrack(index + 1, path)   # Explore
                path.pop()                   # Un-choose (backtrack)

        # \U0001f680 Start recursion from index 0 with an empty path
        backtrack(0, [])

        return res
