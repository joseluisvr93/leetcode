def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    index = len(nums1) - 1

    while index >= 0:
        if i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
        elif i < 0:
            nums1[index] = nums2[j]
            j -= 1
        else:
            nums1[index] = nums1[i]
            i -= 1
        index -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
merge(nums1, m, nums2, n)
print(nums1)

