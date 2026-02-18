if __name__ == '__main__':
    """ 
    x = {} is a dict, not a set, an empty set has to be defined in the following way.
    """
    empty_set = set()

    x = {5, 2, 3}

    x.add(4)
    print(x)
    print(type(x))

    # remove raises KeyError if not found, discard does nothing if not found
    x.remove(4)
    x.discard(4)
    print("after removing 4: ", x)

    x.add(3)
    print("after adding 3: ", x)

    # removes a random value in the set and returns it
    print("popped value", x.pop(), sep=": ")
    print("after popping a random value: ", x)

    print(5 in x)

    print(len(x))

    x = {5, 2, 3}
    y = {8, 2, 9, 3}

    # union of two sets, common elements are removed
    z = x | y
    print(z)

    # find the common elements in both sets
    common_elements = x & y
    print(common_elements)

    # elements in x but not in y
    difference_set = x - y
    print("difference set: ", difference_set)

    # elements in either set but not in both
    symmetric_difference_set = x ^ y
    print("symmetric difference set: ", symmetric_difference_set)

    # shallow copy, only immutable elements can be added to a set
    copx = x.copy()
    print(copx)

    print(sorted(x))

    # sum all the values of a set
    print(sum(x))

    copx.clear()
    print(copx)

