def maxVowels(s, k):
    vowels = "aeiou"
    left, right = 0, k-1
    max_count = 0
    count = 0
    for i in range(right+1):
        if s[i] in vowels:
            count += 1
    max_count = max(count, max_count)
    while right < len(s)-1:
        if s[left] in vowels:
            count -= 1
        if s[right+1] in vowels:
            count += 1
        left += 1
        right += 1
        max_count = max(max_count, count)
    return max_count

s="abciiidef"
k=3
answer = maxVowels(s, k)
print(answer)