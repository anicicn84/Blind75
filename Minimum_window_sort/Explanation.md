## Explanation of the approach

The algorithm needs to go from the start and find the first anomaly when the array is not sorted. 
Also it needs to go from the back to find also the first anomaly from the right side. In this way we get the start and end positions of the unsorted subarray, but this does not mean it is the solution. 
We need to find minimal and maximal elements in the unsorted part of the array so they could find their place in the sorted parts of the array. In this case sorted elements help us to know when to stop and not to go further. 

### A step-by-step algorithm:

1. **Identify the `start` of the Unsorted Subarray:** Iterate from the beginning of the array until we find the first element that is greater than the next element, marking the start of the subarray that needs to be sorted.

2. **Identify the `end` of the Unsorted Subarray:** Similarly, iterate from the end of the array backwards until we find the first element that is less than the previous element, marking the end of the subarray.

3. **Find the Minimum and Maximum within the Unsorted Subarray:** This is because the correct positions of the minimum and maximum elements might require extending the subarray's boundaries to include elements that are not in their correct position when the entire array is sorted. Imagine we have a case `[1, 2, 10, 4, 5, 12, 7, 8, 15]`. Here the unsorted part is `[4, 5, 12]`, but min is `4` and max is `12` and they need to find their correct positions in the sorted paerts of the array: `4` behind `10` and 12 after `8` and `10`.

4. **Extend the Subarray if Necessary:** Adjust the start and end positions identified in steps 1 and 2 if there are elements outside of the identified subarray that are greater than the minimum or less than the maximum within the subarray, like in the example given.

5. **Calculate the Length of the Required Subarray:** Subtract the end position index from the start position index and add 1 due to off-by-one error. 