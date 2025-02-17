class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        final_arr = []
        updated_set = set(nums)
        for i in range(1, len(nums)+1):
            if i not in updated_set:
                final_arr.append(i)
        return final_arr
        