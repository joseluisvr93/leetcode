#Binary search
# def searchInsert(nums, target):
    # left = 0
    # right = len(nums) - 1
    # while left <= right:
        # mid = (left + right) // 2
        # if nums[mid] == target:
            # return mid
        # elif nums[mid] < target:
            # left = mid + 1
        # else:
            # right = mid - 1
    # return left
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    return binarySearch(nums, target, left, right)

def binarySearch(array, x, low, high):
    if high >= low:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, x, low, mid - 1)
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return low

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

