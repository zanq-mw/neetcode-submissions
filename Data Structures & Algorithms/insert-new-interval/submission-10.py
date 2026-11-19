class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        output = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if new_end < start:
                output.append([new_start, new_end])
                return output + intervals[i:]
            elif new_start > end:
                output.append(intervals[i])
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        output.append([new_start, new_end])
        return output
            
            