## Problem statement

Given a linked list, remove the last `nth` node from the end of the list and return the head of the modified list.

Example 1:
---

Input: `list = 1 -> 2 -> 3 -> 4 -> 5`, `n = 2`

Expected Output: `1 -> 2 -> 3 -> 5`

Justification: The 2nd node from the end is "4", so after removing it, the list becomes `[1,2,3,5]`.


Example 2:
---

Input: `list = 10 -> 20 -> 30 -> 40`, `n = 4`

Expected Output: `20 -> 30 -> 40`

Justification: The 4th node from the end is "10", so after removing it, the list becomes `[20,30,40]`.

Example 3:
---

Input: `list = 7 -> 14 -> 21 -> 28 -> 35`, `n = 3`

Expected Output: `7 -> 14 -> 28 -> 35`

Justification: The 3rd node from the end is "21", so after removing it, the list becomes `[7,14,28,35]`.