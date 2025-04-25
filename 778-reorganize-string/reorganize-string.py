class Solution:
    def reorganizeString(self,s):
        # Count frequency of each character
        count = Counter(s)
        
        # Check if any char is too frequent to ever separate
        max_allowed = (len(s) + 1) // 2
        if any(freq > max_allowed for freq in count.values()):
            return ""

        # Build a max-heap (use negative counts because Python heapq is min-heap)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        result = []

        while len(heap) >= 2:
            # Pop top 2 frequent characters
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)

            # Add them to result
            result.append(char1)
            result.append(char2)

            # Decrease frequency and push back if still more left
            if -freq1 > 1:
                heapq.heappush(heap, (freq1 + 1, char1))  # +1 because freq is negative
            if -freq2 > 1:
                heapq.heappush(heap, (freq2 + 1, char2))

        # If one char left, place it at end
        if heap:
            freq, char = heapq.heappop(heap)
            if -freq > 1:
                return ""
            result.append(char)

        return "".join(result)
