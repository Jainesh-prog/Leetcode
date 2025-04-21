from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)

        for pair in dominoes:
            key = tuple(sorted(pair))  # Treat [1,2] and [2,1] as same
            counter[key] += 1

        result = 0
        for freq in counter.values():
            if freq > 1:
                result += freq * (freq - 1) // 2  # Number of unique pairs

        return result
