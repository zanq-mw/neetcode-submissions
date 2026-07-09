class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort(key=lambda x: x[0])
        total = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                total += 1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]

        return total
