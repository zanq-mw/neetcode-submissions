class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap, -num)
        i=1
        while i <k:
            heapq.heappop(maxheap)
            i+=1
        return -heapq.heappop(maxheap)