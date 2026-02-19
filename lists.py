from functools import cmp_to_key
import bisect

def custom_comparator(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    return b[0] - a[0]

class CustomItem:
    def __init__(self, pair):
        self.pair = pair

    def __lt__(self, other):
        if self.pair[0] == other.pair[0]:
            return self.pair[1] > other.pair[1]
        return self.pair[0] > other.pair[0]

if __name__ == '__main__':

    myList = [1, 2, 3, 4, 2]

    # O(1)
    myList.append(4)
    myList.pop()
    print(myList)

    # Concatenate another list to the end, O(k)
    myList.extend([1, 2])

    # Insert at a given position, O(n)
    myList.insert(-1, 5)

    # Remove the first occurrence of a value
    myList.remove(5)

    # Remove by index O(n)
    myList.pop(-1)
    # Remove the last one
    myList.pop()

    # Return the index of the first occurrence of a value O(n)
    print(myList.index(4, 1))

    # Count the number of occurrences of a value, O(n)
    print(myList.count(4))

    # Remove all occurrences of an element in a list, time: O(n), space: O(n)
    removedList = [num for num in myList if num != 4]
    print(removedList)

    # Find indices of all the occurrences of an element, time: O(n), space: O(k)
    foundIndices = [i for i, num in enumerate(myList) if num == 4]

    print(myList.count(4))

    myList = [1, 2, 3, 4]
    print(reversed(myList))

    print("before reversal", myList)
    print(myList.reverse())
    print("after reversal", myList)

    # Difference between list.sort() and sorted(list)
    # sorted returns another list and does not modify the original list
    myList = [4, 3, 2, 1]
    sorted_list = sorted(myList)
    print(sorted_list)

    #list.sort modifies the list in place, and is slightly faster and more memory-efficient
    myList.sort()
    print(myList)

    myList.sort(reverse=True)
    print(myList)

    x = [1, 'a', [1,2,3]]
    print("a list of difference type of elements: ", x)

    x = [1, 2, 2]
    print(x * 2)

    # Swap the elements
    x[1], x[2] = x[2], x[1]

    print(sum(x))

    x = [(2, 3), (2, 7), (2, 5), (5, 3), (4, 8), (3, 1)]
    sorted_list = sorted(x, key=cmp_to_key(custom_comparator))
    print("sorted with custom comparator: ", sorted_list)

    x = [(2, 3), (2, 7), (2, 5), (5, 3), (4, 8), (3, 1)]
    y = []
    for i, pair in enumerate(x):
        y.append(CustomItem(pair))
    print("before sorting: ", [item.pair for item in y])

    new_sorted_list = sorted(y)
    print("sorted list using a custom class: ", [item.pair for item in new_sorted_list])

    pre_filled = [0]
    print(pre_filled * 10)



    # Binary search
    x = [5, 3, 1, 3, 7]
    x.sort()
    print(x)
    print(bisect.bisect_left(x, 3)) # first index ≥ x
    print(bisect.bisect_right(x, 3)) # first index > x
    print("count of 3: ", bisect.bisect_right(x, 3) - bisect.bisect_left(x, 3))
