# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def f(i):
            if i==0:
                return nums[0]
            if i < 0:
                return 0
            if dp[i]!=-1:
                return dp[i]
                
            not_take=f(i-1)
            take = nums[i] + f(i-2)

            dp[i]=max(not_take,take)
            return dp[i]
        return f(n-1)



        