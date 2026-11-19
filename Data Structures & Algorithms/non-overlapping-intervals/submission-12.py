class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        count = 0
        lastmax = intervals[0][1]
        for i in range(1, len(intervals)):
            first, last = intervals[i]
            if first < lastmax:
                lastmax = min(lastmax, last)
                count += 1
            else:
                lastmax = last
        return count