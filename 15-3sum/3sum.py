from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Result list to store triplets

        # Step 1: Sort the input array to enable two-pointer approach
        nums.sort()

        # Step 2: Loop through each number and fix the first element of the triplet
        for i, a in enumerate(nums):
            # Skip duplicate values for the first element
            if i > 0 and a == nums[i - 1]:
                continue

            # Step 3: Use two pointers to find the other two elements
            left, right = i + 1, len(nums) - 1

            while left < right:
                threesum = a + nums[left] + nums[right]

                # Step 4: Move pointers based on the sum
                if threesum > 0:
                    right -= 1  # Sum too big → move right pointer left
                elif threesum < 0:
                    left += 1   # Sum too small → move left pointer right
                else:
                    # Found a valid triplet
                    res.append([a, nums[left], nums[right]])

                    # Move left pointer and skip duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res
