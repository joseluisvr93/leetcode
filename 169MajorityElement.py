# 169. Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Example 1:
# Input: [3,2,3]
# Output: 3

def majorityElement(nums):
    nums.sort()
    print(nums)
    max = 1
    temp = 1
    res = nums[0]
    for i in range(1,len(nums)):
        if nums[i-1] == nums[i]:
            temp += 1
            if temp > max:
                max = temp
                res = nums[i]
        else:
            temp = 1
    return res

nums = [3,2,3]
print(majorityElement(nums))

