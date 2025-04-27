class Solution:
    def permute(self, l: List[int]) -> List[List[int]]:
        # \U0001f525 Core DFS function to generate all permutations
        def dfs(path, used, res):
            # ✅ Base case: if current path has all elements, it's a valid permutation
            if len(path) == len(l):
                res.append(path[:])  # ⚡ Make a deep copy (important!) and add to result
                return

            # \U0001f501 Try every unused element to expand the path
            for i, num in enumerate(l):
                if used[i]:
                    continue  # \U0001f6ab Skip if already used

                # \U0001f4e5 Choose: add num to current path and mark as used
                path.append(num)
                used[i] = True

                # \U0001f525 Explore further with this new choice
                dfs(path, used, res)

                # \U0001f4e4 Un-choose: remove num and mark as unused (backtrack)
                path.pop()
                used[i] = False

        res = []  # \U0001f4dd Final result list to collect all permutations
        dfs([], [False] * len(l), res)  # \U0001f680 Start DFS with empty path and no used elements
        return res
