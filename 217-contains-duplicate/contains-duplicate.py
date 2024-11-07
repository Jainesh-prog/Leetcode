class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = {}
        for num in nums:
            if num in checked and checked[num] >= 1:
                return True
            checked[num] = checked.get(num, 0) + 1
        return False
        