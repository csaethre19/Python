
def calcGcd(num1, num2):
    while (num1 != num2):
        if (num1 > num2):
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

def setUpRsa(p, q):
    list = []
    list.append(p*q)
    totient = (p-1)*(q-1)
    e = 0
    d= 0
    for i in range(2, totient):
        if (calcGcd(i, totient) == 1):
            e = i
            list.append(e)
            break
    for j in range(1, p*q):
        if (((e*j) % totient) == 1):
            d = j
            list.append(d)
            break
    
    return list
def encrypt(m, e, n):
    return (m**e) % n
def decrypt(c, d, n):
    return (c**d) % n

list = setUpRsa(1171, 1181)
print(list)
ciphertext = encrypt(1200, list[1], list[0])
print("ciphertext: " + str(ciphertext))
print("message: " + str(decrypt(ciphertext, list[2], list[0])))