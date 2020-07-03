def namelist(names):
    result = ""
    for el in names:
        people = len(names) - 2
        if (names.index(el) == people):
            result += el['name'] + " & "
        elif (names.index(el) == len(names) - 1):
            result += el['name']
        else:
            result += el['name'] + ", "
    return result
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))