class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        start, end = newInterval
        for i in range(len(intervals)):
            first, second = intervals[i]
            if start > second:
                output.append(intervals[i])
            elif end<first:
                output.append([start, end])
                return output + intervals[i:]
            else:
                start = min(start, first)
                end = max(end, second)

        output.append([start, end])
        return output