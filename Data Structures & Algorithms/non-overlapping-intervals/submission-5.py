class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <2:
            return 0
        count = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        last_max = intervals[0][1]

        for i in range(1, len(intervals)):
            print(intervals[i])
            print(last_max)
            print(count)
            if intervals[i][0] < last_max:
                print("HEY")
                count+=1
                print(count)
                last_max = min(last_max, intervals[i][1])
            else:
                last_max = intervals[i][1]
        
        return count