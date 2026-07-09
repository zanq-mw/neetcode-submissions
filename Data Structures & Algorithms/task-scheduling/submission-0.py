class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        count = Counter(tasks)
        heap = [-task for task in count.values()]

        heapq.heapify(heap)

        q = deque()

        while heap or q:
            
            if q:
                if q[0][1] <= time:
                    heapq.heappush(heap, q.popleft()[0])
            time += 1
            if heap:
                pop = heapq.heappop(heap)
                if pop < -1:
                    q.append([pop+1, time+n])
            
        return time
                

        
