class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        timer = max(endTime) + 1
        starter = min(endTime)
        memo = [0] * timer

        for time in range(starter, timer):
            memo[time] = memo[time-1]
            for i, num in enumerate(endTime):
                if num == time:
                    start = startTime[i]
                    val = profit[i]
                    memo[time] = max(memo[time], val + memo[start])
            
        return memo[-1]