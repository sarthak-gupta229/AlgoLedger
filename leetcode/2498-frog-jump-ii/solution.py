# Runtime: 33 ms
# Memory: 35.9 MB

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n=len(stones)
        ans = 0
        if n==2:
            return stones[n-1]-stones[0]

        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i-2])

        return ans
    

    