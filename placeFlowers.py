def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return "true"
    else:
        for i in range(0, len(flowerbed)):
            if n==0:
                break
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i+1]==0:
                    n = n-1
                elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                    n = n-1
                elif (flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                    n = n-1
    if n == 0:
        return "true"
    else:
        return "false"  
        
flowerbed = [1,0,0,0,1]
n = 2

answer = canPlaceFlowers(flowerbed,n)
print(answer)
