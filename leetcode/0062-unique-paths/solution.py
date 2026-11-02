# Runtime: 1 ms
# Memory: 18.9 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0

                dp[i][j] = up + left

        return dp[m-1][n-1]






        # def f(i,j):
        #     if i >= m or j >= n:
        #         return 0
        #     if i==m-1 and j==n-1:
        #         return 1
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     take=f(i,j+1)
        #     nottake=f(i+1,j)
        #     dp[i][j]=take+nottake
        #     return dp[i][j]
        # return f(0,0)




