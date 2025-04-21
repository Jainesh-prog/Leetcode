class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0  # To store the total count of valid triplets
        n = len(arr)

        # Step 1: Iterate over all possible triplets (i, j, k)
        for i in range(n):
            for j in range(i + 1, n):  # Ensure j > i
                # Early pruning: skip if |arr[i] - arr[j]| > a
                if abs(arr[i] - arr[j]) > a:
                    continue

                for k in range(j + 1, n):  # Ensure k > j > i
                    # Check the remaining two conditions
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                        continue

                    # If all 3 conditions pass, count this triplet
                    ans += 1

        return ans
