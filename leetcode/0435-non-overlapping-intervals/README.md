# 435. Non-overlapping Intervals

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 73 ms |
| Memory | 48.8 MB |
| Submission Date | 2026-10-26T06:21:22.186Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.</p>

<p><strong>Note</strong> that intervals which only touch at a point are <strong>non-overlapping</strong>. For example, <code>[1, 2]</code> and <code>[2, 3]</code> are non-overlapping.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> [1,3] can be removed and the rest of the intervals are non-overlapping.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[1,2],[1,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need to remove two [1,2] to make the rest of the intervals non-overlapping.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code>
- <code>intervals[i].length == 2</code>
- <code>-5 * 10<sup>4</sup> &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>4</sup></code>

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)
