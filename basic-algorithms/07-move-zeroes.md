## Problem: Move Zeroes (Easy)

**Link:** https://leetcode.com/problems/move-zeroes/

### Approach

I use a position pointer to keep track of where the next non-zero element should be placed. When I find a non-zero element, I swap it with the element at the position pointer. This moves all non-zero elements to the front while keeping the zeroes at the end.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

The solution modifies the input array in place and maintains the relative order of the non-zero elements.