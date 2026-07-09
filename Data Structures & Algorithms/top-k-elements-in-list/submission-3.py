class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] +=1

        heap = []
        for key in res:
            heapq.heappush(heap, [res[key], key])
            if len(heap) > k:
                heapq.heappop(heap)
        output = []
        for val, key in heap:
            output.append(key)
        return output