# Runtime: 17 ms
# Memory: 21.8 MB

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        l=0
        r=0
        count=0
        while l<n and r<m:
            if g[l]<=s[r]:
                l+=1
                count+=1
            r+=1
        return count 