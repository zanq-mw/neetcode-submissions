class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]
        count = 0
        total = 0
        visited = set()

        while count < len(points):
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            visited.add(point)
            total += cost
            count += 1
            for i in range(len(points)):
                if i not in visited:
                    nxt = points[i]
                    now = points[point]
                    new = abs(now[0] - nxt[0]) + abs(now[1] - nxt[1])
                    heapq.heappush(heap, (new, i))
        return total