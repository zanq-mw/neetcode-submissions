class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] +=1

        counts = [[] for _ in range(len(nums)+1)]

        for key in res:
            counts[res[key]].append(key)
        
        output = []
        for i in range(len(counts)-1, 0, -1):
            for num in counts[i]:
                output.append(num)
                if len(output) == k:
                    return output