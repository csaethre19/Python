# determines all prime factor decompositions for number n 
# and returns a string that lists them in the following format:
# "(p1**n1)(p2**n2)...(pk**nk)"
def primeFactors(n):
    primeList = []
    result = ""
    for i in range(2, n + 1):
        while (n % i == 0):
            primeList.append(i)
            n = n/i
    if len(primeList) == 0:
        result = "(" + n + ")"
    else:
        count = 1
        for i in range(0, len(primeList), count):
            temp = primeList[i]
            count = 0
            for j in range(i, len(primeList)):
                if (temp == primeList[j]):
                    count = count + 1
            if (count > 1):
                result += "(" + str(temp) + "**" + str(count) + ")"
            else:
                result += "(" + str(temp) + ")"
    return result

def countOdds(n):
    count = 0
    for i in range(0, n):
        if (i % 2 == 1):
            count = count + 1
    return count

print(countOdds(48))
#print(primeFactors(100))
