# Runtime: 3 ms
# Memory: 19.5 MB

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        c=0
        ans=0
        l,r=0,len(tokens)-1
        while l<=r:
            if tokens[l]<=power:
                c+=1
                power-=tokens[l]
                l+=1
                ans=max(ans,c)
            elif c>=1:
                c-=1
                power+=tokens[r]
                r-=1
            else:
                break
        return ans



                




        