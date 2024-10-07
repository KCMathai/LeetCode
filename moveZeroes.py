def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    return nums
nums = [0,1,0,3,12]
answer = moveZeroes(nums)
print(answer)


    # OR


def moveZeroes(nums):
    if len(set(nums)) == 1:
        return nums
    else:   
        left = 0
        right = 1
        while right<len(nums):
            if nums[right] !=0 and nums[left] == 0:
                nums[right], nums[left] = nums[left], nums[right]
                right +=1
                left += 1
            elif nums[right] == 0 and nums[left]!=0:
                left +=1
            else:
                right +=1
        return nums

nums = [0,1,0,3,12]
answer = moveZeroes(nums)
print(answer)

    #or


