class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = 0  # \U0001f4dd To store the maximum length of valid window
        count = collections.defaultdict(int)  # \U0001f9fa Keeps count of fruits in the current window

        l = 0  # \U0001f449 Left pointer for the sliding window

        # \U0001f501 Iterate over tree using right pointer 'r'
        for r, t in enumerate(tree):
            count[t] += 1  # \U0001f9ee Include current fruit 't' in the count

            # \U0001f9f9 If we have more than 2 types of fruits, shrink the window from the left
            while len(count) > 2:
                count[tree[l]] -= 1  # Decrease count of fruit at left pointer
                if count[tree[l]] == 0:
                    del count[tree[l]]  # Remove fruit type if its count becomes zero
                l += 1  # \U0001f9cd‍♂️ Move left pointer forward

            # \U0001f4dd Update maximum fruits we can collect (window size)
            ans = max(ans, r - l + 1)

        return ans  # \U0001f3af Return the maximum fruits collected
