class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        from collections import Counter
        nums_count = Counter(nums)
        sort = sorted(nums_count.items(),key=lambda x:x[0])
        less_nums = {}
        num = 0
        for key,val in sort:
            less_nums[key] = num
            num += val 

        return [less_nums[i] for i in nums]