class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort(key=lambda x: x[0])
        last_max = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_max:
                count += 1
                last_max = min(last_max, intervals[i][1])
            else:
                last_max = intervals[i][1]
        return count