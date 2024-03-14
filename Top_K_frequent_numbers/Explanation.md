## Explanation of the approach

To solve this problem, we can use a hash table to count the frequency of each number in the array, and then use a heap to find the top K frequently occurring numbers.

### A step-by-step algorithm:

1. Iterate through the array and use a hash table (dictionary in Python) to count the frequency of each number.
2. Use a min-heap to keep track of the top K frequent numbers. The heap will contain pairs of (frequency, number).
3. Iterate over the frequency map, and for each entry, add it to the heap. If the heap size exceeds K, remove the smallest element from the heap, ensuring that we always have the top K frequent numbers in the heap.
4. Convert the heap into a list containing just the numbers, which will be our result.


### Algorithm complexity

This solution efficiently finds the top `K` frequently occurring numbers by first counting the frequency of each number using a hash table, and then using a min-heap to find the top `K` frequent numbers. The overall time complexity is `O(NlogK)`, where `N` is the number of numbers in the input array, since we iterate through the array to build the frequency map and then iterate through the map while maintaining a heap of size `K`.