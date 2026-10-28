# Runtime: 20 ms
# Memory: 21.6 MB

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        l,r=0,0
        c=0
        while l<n and  r<m:
            if g[l]<=s[r]:
                l+=1
                c+=1
            r+=1
        return c
        
