if __name__ == '__main__':
    # a tuple is like a list, except it is unmutable
    # and it is more efficient than a list in a situation where the elements do not change

    x = (1, 2, 3, 9, 3)
    y = (3, 4)

    print(x[3:])

    # searching is O(n)
    print("is 9 in x? ", 9 in x)

    print("len is: ", len(x))

    print("index of 9 is: ", x.index(9))

    print("number of occurrence of 3: ", x.count(3))

    print("sorted x: ", sorted(x))

    print("concatenated: ", x + y)

    print("repeated tuple: ", x * 2)

    # Unpacking a tuple
    first, second = y
    print("first value: ", first, "first value: ", second)
