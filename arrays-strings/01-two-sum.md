## Problem: Two Sum (Easy)

**Link:** https://leetcode.com/problems/two-sum/

### Approach

I used a dictionary to store the numbers that have already been seen along with their indices. For each number, I calculate its complement and check whether that complement is already in the dictionary.

### Complexity

- Time: O(n)
- Space: O(n)

### Notes

The solution handles duplicate values correctly. For example, [3, 3] with target 6 returns [0, 1].