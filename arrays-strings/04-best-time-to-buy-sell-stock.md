## Problem: Best Time to Buy and Sell Stock (Easy)

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach

I keep track of the minimum stock price seen so far. For each price, I calculate the possible profit by selling at that price and update the maximum profit found so far.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

The stock must be bought before it is sold. If the prices continuously decrease, the maximum profit remains 0.