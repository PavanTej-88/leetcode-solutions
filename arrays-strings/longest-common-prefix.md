## Problem: Longest Common Prefix (Easy)

**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach

I start with the first string as the current prefix. For each remaining string, I shorten the prefix until the string starts with it. The remaining prefix is the longest common prefix shared by all strings.

### Complexity

- Time: O(n * m)
- Space: O(m)

### Notes

If there is no common prefix, the solution returns an empty string.