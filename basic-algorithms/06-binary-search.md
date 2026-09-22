## Problem: Binary Search (Easy)

**Link:** https://leetcode.com/problems/binary-search/

### Approach

I used two pointers, `left` and `right`, to represent the current search range. I calculate the middle index and compare the middle element with the target. If the target is greater, I search the right half. If it is smaller, I search the left half.

### Complexity

- Time: O(log n)
- Space: O(1)

### Notes

Binary search requires the input array to be sorted. If the target is not present, the solution returns -1.