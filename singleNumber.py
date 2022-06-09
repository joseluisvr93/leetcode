# 136. Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra memory.

def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    counter = {}
    counter2 = {}
    for i in range(len(nums)):
        if counter.get(nums[i]) is None:
            counter[nums[i]] = 1
        else:
            counter[nums[i]] += 1
    for key in counter.keys():
        if counter[key] == 1:
            return key

nums = [2,2,1]
print(singleNumber(nums))

