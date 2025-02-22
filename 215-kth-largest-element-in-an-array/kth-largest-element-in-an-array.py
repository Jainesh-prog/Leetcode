class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]  # Convert to max-heap by negating values
        heapq.heapify(nums)  # Create heap
        
        for _ in range(k - 1):  # Remove k-1 largest elements
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)  # Return k-th largest element