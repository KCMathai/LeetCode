def gcdOfStrings(str1, str2):
    len_1 = len(str1)
    len_2 = len(str2)
    answer = ""
    if len_1 > len_2:
        for i in range(len_2-1, 0, -1):
            if len_2%i == 0 and len_1%i == 0:
                div_1,div_2 = len_1//i, len_2//i
                ans = str2[0:i]
                if ans * div_1 == str1 and ans * div_2 == str2:
                    answer = ans
                    break
    else:
        for i in range(len_1-1, 0, -1):
            if len_2%i == 0 and len_1%i == 0:
                div_1,div_2 = len_1//i, len_2//i
                ans = str2[0:i]
                if ans * div_1 == str1 and ans * div_2 == str2:
                    answer = ans
                    break
    return answer

answer = gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
print(answer)
