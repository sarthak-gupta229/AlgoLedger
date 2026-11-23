# Runtime: 0 ms
# Memory: 19 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return n
        a, b = 1,2 
        for i in range(3,n+1):
            curr= a + b
            a=b
            b=curr
        return b


        