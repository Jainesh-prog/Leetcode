class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-x for x in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            a = heapq.heappop(stones_heap)
            b = heapq.heappop(stones_heap)
            if b > a:
                heapq.heappush(stones_heap, a - b)
        stones_heap.append(0)
        return abs(stones_heap[0])
        