# Runtime: 1 ms
# Memory: 19.5 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[-1]*len(s)
        def f(i,sub):
            if sub != "" and sub[0] == "0":
                return 0
        
            if i == len(s):
                return 1

            if dp[i] != -1:
                return dp[i]
            dp[i]=f(i+1,s[i:i+1])
            if i+1<len(s) and "10" <= s[i:i + 2] <= "26":
                dp[i]+=f(i+2,s[i:i+2])
            return dp[i]
        print(dp)
        return f(0,"")
                
