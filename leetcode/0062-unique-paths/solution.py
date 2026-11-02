# Runtime: 1 ms
# Memory: 19.6 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for _ in range(n)]for _ in range(m)]
        def f(i,j):
            if i >= m or j >= n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            take=f(i,j+1)
            nottake=f(i+1,j)
            dp[i][j]=take+nottake
            return dp[i][j]
        return f(0,0)




        