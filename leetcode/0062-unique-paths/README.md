# 62. Unique Paths

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Combinatorics-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 18.9 MB |
| Submission Date | 2026-11-02T05:44:42.973Z |
| Platform | leetcode |

## Problem Statement

<p>There is a robot on an <code>m x n</code> grid. The robot is initially located at the <strong>top-left corner</strong> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>Given the two integers <code>m</code> and <code>n</code>, return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The test cases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" />
<pre>
<strong>Input:</strong> m = 3, n = 7
<strong>Output:</strong> 28
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Down
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= m, n &lt;= 100</code>

## Solution

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0

                dp[i][j] = up + left

        return dp[m-1][n-1]






        # def f(i,j):
        #     if i >= m or j >= n:
        #         return 0
        #     if i==m-1 and j==n-1:
        #         return 1
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     take=f(i,j+1)
        #     nottake=f(i+1,j)
        #     dp[i][j]=take+nottake
        #     return dp[i][j]
        # return f(0,0)





```

[View on LeetCode](https://leetcode.com/problems/unique-paths/)
