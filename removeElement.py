def removeElement(nums,val):
    if len(nums) == 0:
        return 0
    res = len(nums)-1
    i = len(nums)-1
    j = 0

    while nums[i] == val:
        i-=1
        res -= 1

    while j < i:
        if nums[j] == val:
            res -= 1
            nums[j] = nums[i]
            nums[i] = val
            i-=1
            while nums[i] == val:
                i-=1
                res -= 1
        j+=1
    return res

nums = [3,2,2,3]
val = 2

print(removeElement(nums,val))
print(nums)


        
