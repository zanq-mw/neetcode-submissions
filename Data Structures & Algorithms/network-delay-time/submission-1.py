class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [[0, k]]
        adj = defaultdict(list)
        for src, target, time in times:
            adj[src].append([target, time])
        visited = set()
        total_times = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node in total_times:
                continue
            total_times[node] = time
            for target, time2 in adj[node]:
                if target not in visited:
                    heapq.heappush(heap, [time2+time, target])

        if len(total_times.keys()) != n:
            return -1
        return max(total_times.values())