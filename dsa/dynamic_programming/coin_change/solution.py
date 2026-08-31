class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        inf = amount + 1
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != inf else -1

