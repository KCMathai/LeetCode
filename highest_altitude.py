def largestAltitude(gain):
    maxs = 0
    sums = 0
    for i in gain:
        sums += i
        maxs = max(sums,maxs)
    return maxs

gain = [-5,1,5,0,-7]
answer = largestAltitude(gain)
print(answer)