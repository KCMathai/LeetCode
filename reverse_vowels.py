def reverseVowels(self, s):
        vowels = []
        length =len(s)
        for i in range(length):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                vowels.append(s[i])
        k=len(vowels)-1
        new = ""
        for i in range(length):
            if s[i] in vowels:
                new = new +vowels[k]
                k=k-1
            else:
                new = new + s[i]
        return new





