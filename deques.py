from collections import deque
from collections import Counter
import copy

if __name__ == '__main__':
    d = deque([3, 2, 1])

    # Add element to the end, O(1)
    d.append(4)
    print(d)

    # Add element to the start, O(1)
    d.appendleft(0)
    print(d)

    # Remove element at the end, O(1)
    d.pop()
    print(d)

    # Remove element at the start, O(1)
    d.popleft()
    print(d)

    d.extend([4, 5])
    print(d)

    d.extendleft(reversed([0, 1]))
    print(d)

    print(d.index(2))
    print(d.count(3))

    my_list = list(d)
    print(my_list)
    print(type(my_list))

    my_sorted_list = sorted(list(d))
    print(my_sorted_list)

    sorted_d = deque(my_sorted_list)
    print(sorted_d)