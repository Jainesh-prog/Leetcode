class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0]*(n+1)
        for c in citations:
            count[min(n,c)] += 1

        h = n
        papers = count[n]
        while papers < h:
            h -= 1
            papers += count[h]

        return h
        