class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for start, end, price in flights:
            adj[start].append((end, price))
        
        heap = [(0, src, 0)]
        while heap:
            cost, airport, stops = heapq.heappop(heap)
            if airport == dst:
                return cost
            if stops > k:
                continue
            for end, price in adj[airport]:
                heapq.heappush(heap, (price+cost, end, stops+1))
        
        return -1
