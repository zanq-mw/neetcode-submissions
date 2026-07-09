class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-stone)
        
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first < second:
                new = first - second
                heapq.heappush(heap, new)
            
        if len(heap) == 0:
            return 0
        return -heap[0]
