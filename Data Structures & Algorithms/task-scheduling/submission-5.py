class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        maxheap = []
        for key in counts:
            heapq.heappush(maxheap, -counts[key])
        t = 0
        q = deque()
        while maxheap or q:
            if q and q[0][0] <= t:
                _, num = q.popleft()
                heapq.heappush(maxheap, -num)
            if maxheap:
                num = -heapq.heappop(maxheap)
                if num > 1:
                    q.append([t+n+1,num-1])
            t+=1
        return t