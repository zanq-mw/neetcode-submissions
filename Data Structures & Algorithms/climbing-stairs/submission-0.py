class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
     
        def memoHelper(n):
            if n not in memo:
                memo[n] = memoHelper(n-1) + memoHelper(n-2)
            return memo[n]
        
        return memoHelper(n)

