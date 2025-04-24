from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))

        non_inc = [0] * n
        non_dec = [0] * n

        # Build non-increasing prefix
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_inc[i] = non_inc[i - 1] + 1

        # Build non-decreasing suffix
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1

        result = []
        for i in range(time, n - time):
            if non_inc[i] >= time and non_dec[i] >= time:
                result.append(i)

        return result
