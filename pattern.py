def pattern():
    for i in range(0, 9):
        print("@", end = '')
        for j in range(0, 9):
            if (j == i):
                print("@", end = '')
            else:
                print(".", end = '')
        print("@")
pattern();