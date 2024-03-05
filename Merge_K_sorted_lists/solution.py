import heapq

def merge_k_sorted_lists(lists):
    # Initialize the heap.
    heap = []
    # Fill the heap with the first element of each list along with the index of the list and the element.
    for i, lst in enumerate(lists):
        if lst:  # Check if the list is not empty.
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        result.append(value)
        # If there is a next element in the same list, push it into the heap.
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_value, list_index, element_index + 1))

    return result

# Example usage:
L1 = [2, 6, 8]
L2 = [3, 6, 7]
L3 = [1, 3, 4]
assert(merge_k_sorted_lists([L1, L2, L3]) == [1, 2, 3, 3, 4, 6, 6, 7, 8])

L1 = [5, 8, 9]
L2 = [1, 7]
assert(merge_k_sorted_lists([L1, L2]) == [1, 5, 7, 8, 9])
