# Runtime: 19 ms
# Memory: 19.2 MB

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        answer=[]
        curr=[]
        def f(i,part):
            if len(curr)==4 and i==len(s):
                answer.append(".".join(curr))
                return 
            for j in range(i,len(s)):
                part=s[i:j+1]
                if len(part) > 3:
                    break
                if len(part) > 1 and part[0] == "0":
                    break
                if int(part) > 255:
                    break

                curr.append(part)
                f(j+1,"")
                curr.pop()
        f(0,"")
        return answer
        
        