class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_needed = [10001 for _ in range(amount+1)]
        coins_needed[0] = 0

        for num in range(1, amount+1):
            for coin in coins:
                if coin <= num:
                    coins_needed[num] = min(coins_needed[num], 1 + coins_needed[num-coin])
        if coins_needed[amount] > 10000:
            return -1
        return coins_needed[amount]