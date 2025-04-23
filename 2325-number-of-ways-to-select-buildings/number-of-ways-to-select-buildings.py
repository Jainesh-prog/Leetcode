class Solution:
    def numberOfWays(self, s: str) -> int:
        total_0 = s.count('0')
        total_1 = s.count('1')
        left_0, left_1 = 0 ,0
        ans = 0
        for ch in s:
            if ch == '0':
                ans += (left_1 * (total_1-left_1))
                left_0 += 1
            if ch == '1':
                ans += (left_0 * (total_0-left_0))
                left_1 += 1
        return ans
        