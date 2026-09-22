## Problem: Reverse a Linked List (Easy)

**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach

I use three references: `previous`, `current`, and `next_node`. For each node, I save the next node, reverse the current node's link to point to the previous node, and then move the references forward.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

The list is reversed in place. The solution also handles a linked list containing only one node.