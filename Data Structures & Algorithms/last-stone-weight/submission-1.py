class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        
        while len(maxheap) >1:
            s1 = -heapq.heappop(maxheap)
            s2 = -heapq.heappop(maxheap)
            if s1 > s2:
                heapq.heappush(maxheap, -(s1-s2))
            
        if maxheap:
            return -maxheap[0]
        return 0