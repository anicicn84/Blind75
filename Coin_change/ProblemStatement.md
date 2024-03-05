## Problem statement

Given an infinite supply of `n` coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

Example:

```
Denominations: {1,2,3}
Total amount: 5
Output: 5
```
Explanation: 
```
There are five ways to make the change for '5', here are those ways:
  1. {1,1,1,1,1} 
  2. {1,1,1,2} 
  3. {1,2,2}
  4. {1,1,3}
  5. {2,3}
```


Given a number array to represent different coin denominations and a total amount `T`, we need to find all the different ways to make a change for `T` with the given coin denominations. We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.