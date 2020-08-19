def guessNumbers():
    list = [44, 2, 21, 43, 78, 67, 99, 89]
    answer = 0
    while (str(answer) != "q"):
        answer = input("guess a number from the list\n")
        if (str(answer) == "q"):
            print("thank you, goodbye!")
            break
        elif (int(answer) in list):
            print("you guessed one of the numbers!")
        else:
            print("sorry keep guessing")


#guessNumbers()

def multiplyLists(list_one, list_two):
    final_list = []
    for i in range(0, len(list_one)):
        final_list.append(list_one[i] * list_two[i])
    return final_list

list_one = [8, 19, 148, 4]
list_two = [9, 1, 33, 83]
print(multiplyLists(list_one, list_two))