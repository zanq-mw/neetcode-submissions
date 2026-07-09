class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}



        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            if (i, total) in memo:
                return memo[(i, total)]
            res = 0
            res += dfs(i, total+coins[i])
            res += dfs(i+1, total)
            memo[(i, total)] = res
            return res

        return dfs(0, 0)
        # 1 -> 1
        # 2 -> 2
        # 3 -> 2 or 3
        # 4 -> 