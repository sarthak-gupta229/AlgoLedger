# Runtime: 529 ms
# Memory: 62.1 MB

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        def f(i, target):
            if i == 0:
                return 1 if target % coins[0] == 0 else 0

            if dp[i][target] != -1:
                return dp[i][target]

            notTake = f(i - 1, target)

            take = 0
            if coins[i] <= target:
                take = f(i, target - coins[i])

            dp[i][target] = take + notTake
            return dp[i][target]

        return f(n - 1, amount)