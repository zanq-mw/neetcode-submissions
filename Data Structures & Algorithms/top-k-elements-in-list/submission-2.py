class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] +=1

        return heapq.nlargest(k, res.keys(), key=res.get)