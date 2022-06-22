# 215. Kth Largest Element in an Array

# Given an integer array nums, and an integer k, find the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Example 1:
# Input: nums = [3,2,1,5,6,4] k = 2
# Output: 5

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort(reverse=True)
    return nums[k-1]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
