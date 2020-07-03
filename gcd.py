def calcGcd(a, b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a

def birthdayProb(n):
    days = 365
    for i in range (1, n):
        days = days * (days - 1)
    return days / (365**12)
#print(calcGcd(144, 12))
print(birthdayProb(9))