class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        start, end = newInterval
        while i < len(intervals) and start > intervals[i][1]:
            output.append(intervals[i])
            i +=1
        
        while i < len(intervals) and end >= intervals[i][0]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i+=1
        
        output.append([start, end])

        while i<len(intervals):
            output.append(intervals[i])
            i+=1
        
        return output