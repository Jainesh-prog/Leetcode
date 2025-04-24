class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0  # current length of positive product subarray
        neg = 0  # current length of negative product subarray
        max_len = 0

        for num in nums:
            if num == 0:
                pos, neg = 0, 0  # reset when we hit zero
            elif num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            else:  # num < 0
                pos, neg = (neg + 1 if neg > 0 else 0), pos + 1
            max_len = max(max_len, pos)

        return max_len
