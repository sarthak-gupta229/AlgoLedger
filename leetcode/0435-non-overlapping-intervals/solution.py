# Runtime: 73 ms
# Memory: 48.8 MB

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
            intervals.sort(key= lambda x:x[1])
            last_free=intervals[0][1]
            c=0
            for start,end in intervals[1:]:
                if start>=last_free:
                    last_free=end
                else:
                    c += 1
            return c     