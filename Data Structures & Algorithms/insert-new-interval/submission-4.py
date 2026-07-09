class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        output = []
        for i in range(len(intervals)):
            first, last = intervals[i][0], intervals[i][1]
            if end < first:
                output.append([start, end])
                return output + intervals[i:]

            elif start > last:
                output.append(intervals[i])
            
            else:
                start = min(start, first)
                end = max(end, last)
        
        output.append([start, end])
        return output
                