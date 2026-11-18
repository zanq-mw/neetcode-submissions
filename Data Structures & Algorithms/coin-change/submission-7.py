class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [1001 for _ in range(amount+1)]
        memo[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if coin > i:
                    continue
                memo[i] = min(memo[i], memo[i-coin]+1)
        
        if memo[amount] == 1001:
            return -1
        return memo[amount]