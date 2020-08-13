def multiAdd(*args):
    result = 0
    for x in args:
        result += x
    return result

print(multiAdd(5,6,9,99,2))