## Explanation of the approach

To solve this problem, we can use a two-pointer approach. This method involves placing two pointers at the beginning and end of the array and then moving them towards each other until they meet. The basic idea is to calculate the area formed between the lines pointed by the two pointers at each step and update the maximum area found so far. The key to the two-pointer approach is deciding how to move the pointers.

### A step-by-step algorithm:

- Start with two pointers: one at the beginning of the array (`left`) and one at the end (`right`).
- Calculate the area formed between the lines at the `left` and `right` pointers. The width between the two lines is `right - left`, and the height is the minimum of the two lines because the container can only hold water up to the height of the shorter line. Therefore, the area is `min(height[left], height[right]) * (right - left)`.
- Update the maximum area if the current area is greater than the maximum area found so far.
- Move the pointer pointing to the shorter line towards the other pointer by one step (increment `left` if `height[left] < height[right]`, otherwise decrement `right`). The rationale behind this is that moving the shorter line might give us a chance to find a taller line, which could potentially lead to a larger area. Moving the taller line inward will not increase the area because the height of the container is limited by the shorter line, and the width would only decrease.
We repeat the above steps until the two pointers meet.