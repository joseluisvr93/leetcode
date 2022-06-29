# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively.
# Return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# Example 1:
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1, 2, 3] and median is 2.

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums = nums1 + nums2
    nums.sort()
    if len(nums) % 2 == 0:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    else:
        return nums[len(nums) // 2]

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
