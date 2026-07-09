class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        timer = max(endTime) + 1
        memo = [0 for _ in range(timer)]

        for time in range(1, timer):
            for i in range(len(endTime)):
                if endTime[i] <= time:
                    memo[time] = max(memo[time], profit[i] + memo[startTime[i]])
                
        
        return memo[-1]
