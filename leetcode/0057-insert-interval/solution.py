# Runtime: 2 ms
# Memory: 20.9 MB

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        arr=intervals+[newInterval]
        arr.sort(key=lambda x: x[0])
        result=[]
        for s,e in arr:
            if not result or result[-1][1]<s:
                result.append([s,e])
            else :
                result[-1][1]=max(result[-1][1],e)

        return result

        

        
        