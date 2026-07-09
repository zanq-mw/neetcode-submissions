class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def rebalance(self):
        if len(self.minHeap) > len(self.maxHeap) + 1:
            pop = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -pop)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            pop = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -pop)
    
    def addNum(self, num: int) -> None:
        if self.maxHeap and -num >= self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        self.rebalance()


    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -(self.maxHeap[0])) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            print(self.maxHeap)
            return -(self.maxHeap[0])
        