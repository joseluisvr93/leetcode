# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def twoSum(nums, target):
    rest = {}
    i = 0
    for num in nums:
        r = target - num
        if rest.get(r) == None:
            rest[r] = i
        i += 1
    i = 0
    print(rest)
    for num in nums:
        if rest.get(num) != None:
            if rest.get(num) != i:
                return [i,rest[num]]
        i += 1


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
