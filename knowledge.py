
if __name__ == '__main__':
    """
    Mutable: list, dict, set
    Inmutable: int, string, bool, noneType, float, tuple
    """

    """
    is: checks if two objects point to the same reference, mainly used for two things:
    1. If  x is None (to check None type)
    2. if children1 is class2 (if children1 is an instance of class2)
    """
    x = 3
    print(x is None)

    print(type(x) is int)


    """
    The keyword not is THE negation in python
    ! is only used with the operator != to check for inequality, other than that, use not
    """

    """
    Tenary Operator:  a if condition else b 
    """
    x = 0 if 1 > 2 else 2
