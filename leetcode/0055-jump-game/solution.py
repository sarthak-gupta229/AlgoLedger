# Runtime: 21 ms
# Memory: 20.3 MB

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        # max_idx is how much max we can junp till which idx
        max_idx=0
        for i in range(n):
            if max_idx<i:
                return False
            max_idx=max(max_idx,i+nums[i])
        return True

        