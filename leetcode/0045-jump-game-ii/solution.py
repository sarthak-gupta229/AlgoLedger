# Runtime: 4 ms
# Memory: 20 MB

class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        jump=0
        l,r=0,0
        while r<n-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            jump+=1
        return jump
        