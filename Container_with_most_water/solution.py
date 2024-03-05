def calculateArea(left_idx, right_idx, heights):
    min_height = min(heights[right_idx], heights[left_idx])
    return (right_idx - left_idx) * min_height


def incrementSmallerIdx(left_idx, right_idx, heights):
    if heights[left_idx] < heights[right_idx]:
        left_idx += 1
    else:
        right_idx -= 1
    return left_idx, right_idx


def maxArea(heights):
    left_idx = 0
    right_idx = len(heights) - 1
    
    maxArea = 0
    while left_idx < right_idx:
        current_area = calculateArea(left_idx, right_idx, heights)
        if current_area > maxArea:
            maxArea = current_area
        left_idx, right_idx = incrementSmallerIdx(left_idx, right_idx, heights)
    return maxArea
    
test_set1 = [1,3,2,4,5]
expected_output1 = 9
assert(maxArea(test_set1) == expected_output1)

test_set2 = [5,2,4,2,6,3]
expected_output2 = 20
assert(maxArea(test_set2) == expected_output2)

test_set3 = [2,3,4,5,18,17,6]
expected_output3 = 17
assert(maxArea(test_set3) == expected_output3)