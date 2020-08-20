import random

def hangman():
    words = [
        "coyote",
        "clam",
        "satisfaction",
        "moonlight",
        "difinitive",
        "luxury",
        "challenge",
        "kangeroo",
        "xenophobe"
    ]
    word = random.choice(words)
    wrong = 0
    stages = ["",
              "__________         ",
              "|                  ",
              "|        |         ",
              "|        O         ",
              "|      / | \\      ",
              "|       / \\       ",
              "|                  "
            ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False;
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            for i in range(0, len(rletters)):
                if (rletters[i] == char):
                    board[i] = char
                    rletters[i] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! it was {}.".format(word))


hangman()