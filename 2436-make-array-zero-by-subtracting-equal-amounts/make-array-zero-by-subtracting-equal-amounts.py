class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        my_set = {x for x in nums if x!=0}
        return len(my_set)
        