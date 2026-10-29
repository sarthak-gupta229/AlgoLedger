# Runtime: 9 ms
# Memory: 23.3 MB

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result=[]
        for s,e in intervals:
            if not result or result[-1][1]<s:
                result.append([s,e])
            else :
                result[-1][1]=max(result[-1][1],e)

        return result