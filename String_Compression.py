
def compress(chars):
    length = len(chars)
    if length < 2:
        return length
    i = j = 0
    while i<length:
        count = 1
        while i<length-1 and chars[i] == chars[i+1]:
            count += 1
            i += 1
        chars[j] = chars[i]
        j +=1
        if count>1:
            str_len = str(count)
            for word in str_len:
                chars[j] = word
                j+=1
        i += 1
    return j

answer = compress(["a","a","b","b","c","c","c"])
print(answer)