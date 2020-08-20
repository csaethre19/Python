import csv

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three", "four"])
    w.writerow(["five", "six", "seven", "eight"])

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))