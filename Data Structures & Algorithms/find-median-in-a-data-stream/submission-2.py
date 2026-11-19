class MedianFinder:

    def __init__(self):
        self.lower = []
        self.higher = []

    def rebalance(self):
        if len(self.lower) > len(self.higher) + 1:
            num = -heapq.heappop(self.lower)
            heapq.heappush(self.higher, num)
        if len(self.higher) > len(self.lower) +1:
            num = -heapq.heappop(self.higher)
            heapq.heappush(self.lower, num)

    def addNum(self, num: int) -> None:
        if self.lower and num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)
        self.rebalance()

        

    def findMedian(self) -> float:
        if len(self.higher) > len(self.lower):
            return self.higher[0]
        elif len(self.lower) > len(self.higher):
            return -self.lower[0]
        return (self.higher[0] + -self.lower[0])/2