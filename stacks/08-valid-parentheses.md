## Problem: Valid Parentheses (Easy)

**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach

I use a stack to store opening brackets. When I encounter a closing bracket, I check whether it matches the most recent opening bracket in the stack. If it does, I remove the opening bracket. At the end, the stack must be empty for the parentheses to be valid.

### Complexity

- Time: O(n)
- Space: O(n)

### Notes

The stack follows the Last In, First Out (LIFO) principle, which makes it suitable for checking matching brackets.