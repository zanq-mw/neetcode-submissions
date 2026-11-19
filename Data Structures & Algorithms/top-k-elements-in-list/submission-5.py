class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] -= 1
        heap = []
        for key in dic:
            heapq.heappush(heap, [dic[key], key])

        res = []
        while len(res) < k and heap:
            res.append(heapq.heappop(heap)[1])

        return res