from heapq import *

class Solution:
  def findTopKFrequentNumbers(self, nums, k):
    topNumbers = []
    
    numFrequencyMap = {}
    for num in nums:
        if num not in numFrequencyMap:
            numFrequencyMap[num] = 0
        numFrequencyMap[num] += 1
    
    minHeap = []
    for num, frequency in numFrequencyMap.items():
        # frequency here is the main minHeap element
        heappush(minHeap, (frequency, num))
        # Since we are in the for loop, we keep adding new elements to the heap, but removing the smallest ones until k elements
        if len(minHeap) > k:
            heappop(minHeap) # remove the last frequent element, we do not need it
            
    topNumbers = []
    while minHeap:
        frequency, num = heappop(minHeap)
        topNumbers.append(num)
    return topNumbers

solution = Solution()

# Example 1
nums1, k1 = [1, 3, 5, 12, 11, 12, 11], 2
print(solution.findTopKFrequentNumbers(nums1, k1))  # Output: [12, 11]

# Example 2
nums2, k2 = [5, 12, 11, 3, 11], 2
print(solution.findTopKFrequentNumbers(nums2, k2))  # Output: [11, 5] or [11, 12] or [11, 3]
