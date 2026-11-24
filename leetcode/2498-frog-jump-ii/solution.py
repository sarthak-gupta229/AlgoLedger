# Runtime: 40 ms
# Memory: 35.9 MB

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans = 0

        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i-2])

        return max(ans, stones[1] - stones[0])
    

    