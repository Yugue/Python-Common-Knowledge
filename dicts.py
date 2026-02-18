import copy
from collections import defaultdict

if __name__ == '__main__':
    x = {'a': 1, 'b': 2}

    # Accessing a value that does not exist in a dict returns an exception

    # Increment or decrement a value directly"
    x["a"] += 1
    x["a"] -= 1

    print(x['a'])

    x['c'] = 3
    print(x)

    # deleting an empty key also results in an exception
    del x['c']
    print(x)

    print(len(x))

    print("c" in x)

    for k, v in x.items():
        print(k, ": ", v)

    for i, (k, v) in enumerate(x.items()):
        print("at index: ", i, "is item: ", k, v)

    # Shallow copy, modifying the original x will change y
    # as well, but since integer is immutable, y does not change
    y = x.copy()
    x['b'] = 3
    print(x)
    print(y)

    # Shallow copy, modifying the original x will change y
    # because list is mutable
    x = {'a': [1, 2, 3], 'b': [4, 5]}
    y = x.copy()
    x['a'].extend([7, 8])
    print(y)

    y.clear()
    print("x", x, sep=": ")

    # Mutable: list, dict, set
    # Immutable: int, string, bool, noneType, float, tuple

    # This is a reference, meaning change in x will reflect in y and vice versa
    # when creating a shallow copy, only change in the original data structure will
    # change the copy's value.
    y = x
    x['a'] = [2]
    print(y)

    y = copy.deepcopy(x)
    x['a'] = [1, 2]
    print(y)

    # Defaultdict allows to specify a default value without the valueNotFound exception
    # the function argument is the default value. For int, since it defaults to 0, we
    # can just add values to a non-existing key. Otherwise, it would throw a value not exist exception.
    # Same with list, it would default to an empty list.
    x = defaultdict(int)
    x['a'] += 1
    print(x)

    y = defaultdict(list)
    y['b'].append(3)
    print(y)