def findMaxAverage(nums, k):
    start = 0
    end = k-1
    max_sum = -1000000000.00000
    sums = 0.00000
    for i in range(start,end+1):
        sums += nums[i]
    max_sum = max(sums, max_sum)
    end += 1
    while end < len(nums):
        sums = sums - nums[start]
        sums = sums + nums[end]
        max_sum = max(sums, max_sum)
        start += 1
        end += 1
    max_average = max_sum/k
    return max_average

nums = [0,1,0,3,12]
answer = findMaxAverage(nums, k=3)
print(answer)
