def kidsWithCandies(candies, extraCandies):
        answer = []
        dup_candies = candies
        j=True
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies
            if candies[i] >= max(dup_candies):
                j=True
            else:
                j=False
            answer.append(j)
        return answer


candles = [2,3,5,1,3]
extraCandles = 3
answer = kidsWithCandies(candles,extraCandles)
print(answer)