class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            first, last = intervals[i]
            if first > output[-1][1]:
                output.append(intervals[i])
            else:
                output[-1][1] = max(output[-1][1], last)
        return output
