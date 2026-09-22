## Problem: Valid Anagram (Easy)

**Link:** https://leetcode.com/problems/valid-anagram/

### Approach

I used a dictionary to count the frequency of each character in the first string. I then decreased the count for each character in the second string and checked whether all character counts matched.

### Complexity

- Time: O(n)
- Space: O(n)

### Notes

The strings must have the same length to be anagrams. The solution also handles characters that appear multiple times.