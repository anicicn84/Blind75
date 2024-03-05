import heapq

def sort(arr):
    
    # Initial indices of the start and end, let's make them negative to be sure
    start = -1
    end = -1
    
    # Find the first element from the start of the array that is greater than the next one
    for idx in range(len(arr) - 1):
        if arr[idx] > arr[idx+1]:
            start = idx
            break
    if start == -1:
        return 0
    
    # Find the first element from the end of the array that is greater than the previous one
    for idx in range(len(arr) - 1, 0, -1): # Take len(arr) - 1 here since we start from this element and thus we include it
        if arr[idx] < arr[idx-1]:
            end = idx
            break
    
    # Now, this unsorted array might contain elements that are greater than or less than the elements
    # in the sorted part of the array. We need to find the first element on the left that is smaller than the
    # minimum of the subarray and find the first element on the right that is greater than max of the subarray
    # to place our positions (start, end) there.
    min_in_unsorted_part = min(arr[start:end+1])
    max_in_unsorted_part = max(arr[start:end+1])
    
    for idx in range(start):
        if arr[idx] > min_in_unsorted_part:
            start = idx
            break
    
    for idx in range(len(arr) - 1, end, -1): # Take len(arr) - 1 here since we start from this element and thus we include it
        if arr[idx] < max_in_unsorted_part:
            end = idx
            break
    
    return end - start + 1
        

test_case1 = [1, 2, 5, 3, 7, 10, 9, 12]
test_case2 = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
test_case3 =[1, 3, 2, 0, -1, 7, 10]
test_case4 = [1, 2, 3]
test_case5 = [3, 2, 1]
assert(sort(test_case1) == 5)
assert(sort(test_case2) == 6)
assert(sort(test_case3) == 5)
assert(sort(test_case4) == 0)
assert(sort(test_case5) == 3)

