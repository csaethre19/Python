import os
import csv

def readFurnitureReqeusts():
    path = os.path.join("C:\\", "Users", "charl", "Documents", "furniture_requests081320.txt")
    with open(path, "r") as f:
        print(f.read())

def writeUserInputToFile():
    answer = input("Where were you born?")
    with open("user_birthplace.txt", "w") as f:
        f.write(answer)


#writeUserInputToFile()

def write_lists_to_CSV():
    lists = [
        ["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man On Fire", "Flight"]
    ]
    with open("movies.csv", "w", newline='') as f:
        w = csv.writer(f, delimiter=",")
        for row in lists:
            w.writerow(row)
            

write_lists_to_CSV()
