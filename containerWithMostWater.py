def maxArea(height):
    max_water = 0
    left = 0
    right = len(height)-1
    while left<right:
        min_height = min(height[left],height[right])
        water = min_height * (right - left)
        max_water = max(water, max_water)
        if min_height == height[left]:
            left += 1
        else:
            right -= 1
    return max_water

height = [1,8,6,2,5,4,8,3,7]
answer = maxArea(height)
print(answer)