# 198. House Robber

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.1 MB |
| Submission Date | 2026-11-24T17:06:03.151Z |
| Platform | leetcode |

## Problem Statement

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <b>without alerting the police</b></em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 100</code>
- <code>0 &lt;= nums[i] &lt;= 400</code>

## Solution

```py
class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[-1 for _ in range(n)]
        def f(i):
            if i==0:
                return nums[i]
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            skip=f(i-1)
            take=nums[i]+f(i-2)
            dp[i]=max(skip,take)
            return dp[i]
        return f(n-1)
            


        
```

[View on LeetCode](https://leetcode.com/problems/house-robber/)
