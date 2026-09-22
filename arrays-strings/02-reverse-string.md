## Problem: Reverse String (Easy)

**Link:** https://leetcode.com/problems/reverse-string/

### Approach

I used two pointers, one starting from the beginning of the string and the other from the end. I swapped the characters at both positions and moved the pointers toward the center until the entire string was reversed.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

The solution modifies the input list in place. The edge case of a single-character string does not require any swaps.