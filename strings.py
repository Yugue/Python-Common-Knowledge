from collections import Counter

if __name__ == '__main__':
    x = "abc"
    y = "def"

    print(x + y)
    # immutable

    print(len(x))
    print(len(y))

    print(x[-1])
    # string slicing, the last index is exclusive
    print(y[0:2])

    print(x[-1:])
    print(x[1:])

    print("does x start with ab: ", x.startswith("ab"))
    print("does y start with ab: ", y.startswith("ab"))

    x = "adee … fijj … knoo … pstt"
    # immutable
    split_x = (x.split(" … "))
    print(split_x)

    print("Does X starts with adee: ", x.startswith("adee"))

    x = ", ".join(split_x)
    print(x)

    # find returns -1 if a substring is not found, index returns ValueError if a substring is not found
    print(x.find("knoo"))
    print(x.index("knoo"))

    x = "11122222648486"
    # Immutable
    print(x.replace("6", "1"))
    print("After replacing 6 with 1: ", x)

    print("a".upper())
    print("B".lower())

    x = "    11122222648486"
    # Remove trailing or tailing substrings if found. If nothing provided, remove whitespace
    print(x.strip())
    print(x.strip("1"))
    print(x.strip("6"))

    x = "111222226484864"
    print("the number of appearances of substring 64: ", x.count("64"))

    # Counter is literally like a dict
    occurrences = Counter(x)
    print("most 2 common occurrences: ", occurrences.most_common(2))
    print("occurrence Counter: ", Counter(x))
