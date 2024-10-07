def successfulPairs(spells, potions, success):
    answer = []
    last = len(potions)
    potions.sort()
    for i in spells:
        if i*potions[last-1]>=success:
            l , r = 0, last-1
            index = 0
            while l<=r:
                m = (l+r)//2
                if i*potions[m] >= success:
                    r = m-1
                    index = m
                else:
                    l = m+1
            answer.append(last-index)
        else:
            answer.append(0)
    return answer


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
answer = successfulPairs(spells, potions, success)
print(answer)