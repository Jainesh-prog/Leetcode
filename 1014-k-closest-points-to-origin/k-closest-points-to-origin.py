class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i,j in points:
            dist = (i**2)+(j**2)
            minHeap.append([dist,i,j])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist,i,j = heapq.heappop(minHeap)
            res.append([i,j])
            k -= 1
        return res