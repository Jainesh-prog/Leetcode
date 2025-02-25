class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def pair(i):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            pair(i+1)

            subset.pop()
            pair(i+1)
        
        pair(0)
        return res
        