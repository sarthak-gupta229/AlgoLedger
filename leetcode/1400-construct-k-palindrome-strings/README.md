# 1400. Construct K Palindrome Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 45 ms |
| Memory | 19.8 MB |
| Submission Date | 2026-10-29T11:23:09.846Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code> and an integer <code>k</code>, return <code>true</code> if you can use all the characters in <code>s</code> to construct <strong>non-empty</strong> <code>k</code> <span data-keyword="palindrome-string">palindrome strings</span> or <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;annabelle&quot;, k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> You can construct two palindromes using all characters in s.
Some possible constructions &quot;anna&quot; + &quot;elble&quot;, &quot;anbna&quot; + &quot;elle&quot;, &quot;anellena&quot; + &quot;b&quot;
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to construct 3 palindromes using all the characters of s.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;true&quot;, k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> The only possible solution is to put each character in a separate string.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
- <code>s</code> consists of lowercase English letters.
- <code>1 &lt;= k &lt;= 10<sup>5</sup></code>

## Solution

```py
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq={}
        if k>len(s):
            return False
        for i in  s:
            freq[i]=freq.get(i,0)+1
        odd=0
        for i in freq:
            if freq[i]%2!=0:
                odd+=1
        return k>=odd
            
        
```

[View on LeetCode](https://leetcode.com/problems/construct-k-palindrome-strings/)
