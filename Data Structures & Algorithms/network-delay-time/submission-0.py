class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for start, dest, time in times:
            adj[start].append([dest, time])

        heap = [[0, k]]
        shortest_times = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in shortest_times:
                continue
            shortest_times[node] = time
            for nxt, t in adj[node]:
                heapq.heappush(heap, [t+time, nxt])
        for i in range(1, n+1):
            if i not in shortest_times:
                return -1
        return max(shortest_times.values())