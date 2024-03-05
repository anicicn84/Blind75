## Explanation of the approach

To merge `K` sorted lists into a single sorted list, a practical approach is to use a **min-heap**. A min-heap is a binary tree-based data structure that allows us to efficiently find and remove the smallest element. This property is particularly useful for our problem because we can maintain a heap of the smallest elements from each list and repeatedly extract the minimum to build the merged list.

### A step-by-step algorithm:

1. Initialize a min-heap: This heap will store tuples of the form (value, list_index, element_index), where:
`value` is the element from one of the lists,
`list_index` is the index of that list among all the lists we are merging,
`element_index` is the index of the element in its own list.
This setup helps us keep track of which element from which list is currently in the heap and its position.
2. Heapify with the first element of each list: Start by inserting the first element of each list into the heap. This step initializes the heap with the smallest element from each list.
3. Extract and insert:
Repeatedly extract the minimum element from the heap. The [heapq](https://docs.python.org/3/library/heapq.html) module in Python automatically ensures that the heap property is maintained after each extraction.
After extracting an element `(value, list_index, element_index)`, insert the next element from the same list (`list_index`) into the heap, if any. This next element would be at `element_index + 1` in its list.
4. Build the result list: Each time an element is extracted from the heap, append it to the result list. Continue this process until the heap is empty.

## Compile C++ code

To compile C++ code use the following command:

``` 
g++ -o solution solution.cpp -std=c++20
```