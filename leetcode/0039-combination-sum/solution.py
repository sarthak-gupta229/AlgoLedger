# Runtime: 9 ms
# Memory: 19.7 MB

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        arr=[]
        curr=[]
        def f(i,total):
            if total==target:
                ans.append(curr.copy())
                return 
            if i>=len(candidates) or total>target:
                return 
            for num in range(i,len(candidates)):
                curr.append(candidates[num])
                f(num,total+candidates[num])
                curr.pop()
        f(0,0)
        return ans
            