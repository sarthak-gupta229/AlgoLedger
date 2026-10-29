# Runtime: 45 ms
# Memory: 19.8 MB

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq={}
        if k>len(s):
            return False
        for i in  s:
            freq[i]=freq.get(i,0)+1
        odd=0
        for i in freq:
            if freq[i]%2!=0:
                odd+=1
        return k>=odd
            
        