class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        heap = [(0, 0)]
        visited = set()
        count=0
        total_cost = 0


        while count < len(points):
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            total_cost += cost
            visited.add(point)
            count+=1
            for i in range(len(points)):
                if i not in visited:
                    new_cost = abs(points[point][0] - points[i][0]) + abs(points[point][1] - points[i][1])
                    heapq.heappush(heap, (new_cost, i))

        return total_cost