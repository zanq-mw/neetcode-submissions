class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for start, end, price in flights:
            adj[start].append([end, price])
        heap = [[0, src, 0]]
        # total_cost = 0
        while heap:
            cost, node, count = heapq.heappop(heap)
            if node == dst:
                return cost
            if count > k:
                continue
            for end, price in adj[node]:
                heapq.heappush(heap, [cost+price, end, count+1])
        return -1

