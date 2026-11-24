# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[-1 for _ in range(n)]
        def f(i):
            if i==0:
                return nums[i]
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            skip=f(i-1)
            take=nums[i]+f(i-2)
            dp[i]=max(skip,take)
            return dp[i]
        return f(n-1)
            


        