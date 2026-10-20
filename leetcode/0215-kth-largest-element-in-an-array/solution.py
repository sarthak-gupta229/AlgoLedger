# Runtime: 230 ms
# Memory: 35 MB

import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        l = heapq.nlargest(k, nums)
        return l[-1]

        