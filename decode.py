def decodeString(s):
    stack = []
    for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            substring = ""
            while stack[-1] != "[":
                substring = stack.pop() + substring
            stack.pop() # Remove the [
            
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substring)
    return "".join(stack)

answer = decodeString(s="3[a2[c]]")
print(answer)