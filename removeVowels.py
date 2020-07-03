def disemvowel(string):
    result = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(string)):
        temp = string[i]
        for j in range(0, len(vowels)):
            if (ignoreCase(string[i]) == vowels[j]):
                temp = ""
        result += temp
    string = result
    return string

def ignoreCase(char):
    return char.lower()
print(disemvowel("This is It Guys!"))