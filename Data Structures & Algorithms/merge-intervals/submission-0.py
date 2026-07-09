class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        results = []
        for i in intervals:
            if results and results[-1][1] >= i[0]:
                results[-1][1] = max(results[-1][1], i[1])
            else:
                results.append(i)
        return results