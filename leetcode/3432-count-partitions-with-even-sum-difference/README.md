# 3432. Count Partitions with Even Sum Difference

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Prefix_Sum-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 19 MB |
| Submission Date | 2026-10-29T18:10:51.004Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>A <strong>partition</strong> is defined as an index <code>i</code> where <code>0 &lt;= i &lt; n - 1</code>, splitting the array into two <strong>non-empty</strong> subarrays such that:</p>

<ul>
	<li>Left subarray contains indices <code>[0, i]</code>.</li>
	<li>Right subarray contains indices <code>[i + 1, n - 1]</code>.</li>
</ul>

<p>Return the number of <strong>partitions</strong> where the <strong>difference</strong> between the <strong>sum</strong> of the left and right subarrays is <strong>even</strong>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [10,10,3,7,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The 4 partitions are:</p>

<ul>
	<li><code>[10]</code>, <code>[10, 3, 7, 6]</code> with a sum difference of <code>10 - 26 = -16</code>, which is even.</li>
	<li><code>[10, 10]</code>, <code>[3, 7, 6]</code> with a sum difference of <code>20 - 16 = 4</code>, which is even.</li>
	<li><code>[10, 10, 3]</code>, <code>[7, 6]</code> with a sum difference of <code>23 - 13 = 10</code>, which is even.</li>
	<li><code>[10, 10, 3, 7]</code>, <code>[6]</code> with a sum difference of <code>30 - 6 = 24</code>, which is even.</li>
</ul>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No partition results in an even sum difference.</p>
</div>

<p>
```

**Example 3:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,4,6,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All partitions result in an even sum difference.</p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>2 &lt;= n == nums.length &lt;= 100</code>
- <code>1 &lt;= nums[i] &lt;= 100</code>

## Solution

```py
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)

        if total % 2 == 0:
            return len(nums) - 1

        return 0
            
```

[View on LeetCode](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)
