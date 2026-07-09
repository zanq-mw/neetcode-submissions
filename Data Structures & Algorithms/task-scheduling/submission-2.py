from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = []
        for count in counts.values():
            heapq.heappush(heap, -count)

        q = deque()
        timer = 0
        while q or heap:
            if q and q[0][1] == timer:
                t = q.popleft()
                heapq.heappush(heap, t[0])
            if heap:
                t = heapq.heappop(heap)
                if t < -1:
                    q.append((t+1, timer + 1 + n))
            timer += 1
        return timer