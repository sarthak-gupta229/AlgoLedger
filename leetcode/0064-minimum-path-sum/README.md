# 64. Minimum Path Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 46 ms |
| Memory | 23.2 MB |
| Submission Date | 2026-11-25T06:43:24.339Z |
| Platform | leetcode |

## Problem Statement

<p>Given a <code>m x n</code> <code>grid</code> filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> grid = [[1,2,3],[4,5,6]]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 &lt;= m, n &lt;= 200</code>
- <code>0 &lt;= grid[i][j] &lt;= 200</code>

## Solution

```py
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for _ in range(m)]for _ in range(n)]
        def f(i,j):
            if i>=n or j>=m:
                return float('inf')
            if i==n-1 and j==m-1:
                return grid[n-1][m-1]
            if dp[i][j]!=-1:
                return dp[i][j]
            right=grid[i][j]+ f(i,j+1)
            down=grid[i][j]+ f(i+1,j)
            dp[i][j]=min(right,down)
            return dp[i][j]
        return f(0,0)
        
```

[View on LeetCode](https://leetcode.com/problems/minimum-path-sum/)
