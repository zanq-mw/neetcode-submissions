"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = defaultdict(list)
        for i, interval in enumerate(intervals):
            start, end = interval.start, interval.end
            times[start].append(i)
            times[end].append(i)
        res = 0
        sort = sorted(times.keys())
        s = set()
        for t in sort:
            for meet in times[t]:
                if meet in s:
                    s.remove(meet)
                else:
                    s.add(meet)
            res = max(res, len(s))

        return res

