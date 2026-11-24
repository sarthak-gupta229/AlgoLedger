# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1 for _ in range(n+1)]
        def f(i):
            if i==0:
                return 1
            if i==1:
                return 1
            if dp[i]!=-1:
                return dp[i]
            ans=f(i-1)+f(i-2)
            dp[i]=ans
            return dp[i]
        return f(n)
        