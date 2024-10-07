def pivotIndex(nums):
    rollsum1 = 0
    rollsum2 = 0
    index = -1
    for i in range(len(nums)):
        rollsum1 += nums[i]
    for i in range(len(nums)):
        if i == 0:
            rollsum1 = rollsum1 - nums[0]
        else:
            rollsum1 -= nums[i]
            rollsum2 += nums[i-1]
        if rollsum1 == rollsum2:
            index = i
            break
    return index

nums = [1,7,3,6,5,6]
answer = pivotIndex(nums)
print(answer)