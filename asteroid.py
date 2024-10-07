def asteroidCollision(asteroids):
    stack = []
    for num in asteroids:
        while stack and stack[-1] > 0 and num < 0:
            if abs(num) > abs(stack[-1]):
                stack.pop()  # Asteroid on stack is destroyed
            elif abs(num) == abs(stack[-1]):
                stack.pop()  # Both asteroids are destroyed
                num = 0  # Stop considering current asteroid
                break
            else:
                num = 0  # Current asteroid is destroyed
                break  # Stop considering current asteroid
        if num: 
            # print(num) # If current asteroid is not destroyed, add it to stack
            stack.append(num)
        # print(stack)
    return stack

asteroids = [10,2,-5]
answer = asteroidCollision(asteroids)
print(answer)