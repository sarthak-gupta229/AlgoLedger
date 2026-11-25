# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def check(s,e):
            dp=[-1 for _ in range(n)]
            def f(i):
                if i==s:
                    return nums[i]
                if i<s:
                    return 0
                if dp[i]!=-1:
                    return dp[i]
                nottake=f(i-1)
                if i>=2:
                    take=nums[i]+f(i-2)
                else:
                    take=float('-inf')
                dp[i]=max(take,nottake)
                return dp[i]
            return f(e)
        case1=check(0,n-2)
        case2=check(1,n-1)
        return max(case1,case2)

                
        