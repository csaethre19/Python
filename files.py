import os
path = os.path.join("Users", "charl", "Documents")

with open("st.txt", "w") as f:
    f.write("Hi there!")

my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)