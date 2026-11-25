# Runtime: 46 ms
# Memory: 23.2 MB

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for _ in range(m)]for _ in range(n)]
        def f(i,j):
            if i>=n or j>=m:
                return float('inf')
            if i==n-1 and j==m-1:
                return grid[n-1][m-1]
            if dp[i][j]!=-1:
                return dp[i][j]
            right=grid[i][j]+ f(i,j+1)
            down=grid[i][j]+ f(i+1,j)
            dp[i][j]=min(right,down)
            return dp[i][j]
        return f(0,0)
        