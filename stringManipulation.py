def printCamusChar():
    string = "Camus"
    for s in string:
        print(s)

def newString():
    response_one = input("enter your first response\n")
    response_two = input("enter your second response\n")
    print("Yesturday I wrote a " + response_one + ". I sent it to " + response_two + "!")

#newString()

def capFirstLetter(str):
    return str.capitalize()

#print(capFirstLetter("aldous huxley"))

def stringToList(str):
    list = str.split("? ")
    return list

#print(stringToList("Where now? Who now? When now?"))

def grammaticalSentence(list):
    list.pop()
    sentence = " ".join(list)
    sentence += "."
    return sentence


list = ["The", "fox", "jumped", "over", "the", "fence", "."]
#print(grammaticalSentence(list))

def replace(string):
    result = ""
    for s in string:
        if (s == "s"):
            result += "$"
        else:
            result += s
    return result

#print(replace("A screaming comes across the sky."))

def findFirstM(string):
    index = 0
    for i in range(0, len(string)):
        if (string[i] == "m"):
            index = i
    return index

#print(findFirstM("Hemingway"))
def slice():
    string = "It was a bright cold day in April, and the clocks were striking thirteen."
    result = ""
    for i in range(0, len(string)):
        if (string[i] == ","):
            result = string[:i]
    print(result)

slice()

