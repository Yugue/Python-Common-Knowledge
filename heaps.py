from collections import deque
from collections import Counter
import copy
import heapq

class CustomItem:
    def __init__(self, pair):
        self.pair = pair

    def __lt__(self, other):
        if self.pair[0] == other.pair[0]:
            return self.pair[1] > other.pair[1]
        return self.pair[0] > other.pair[0]

if __name__ == '__main__':
    heap = []
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 2)
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))

    list = [5, 3, 9, 1, 2]
    heapq.heapify(list)
    print(list)
    heapq.heapreplace(list, 7)
    print(list)

    print(heapq.nlargest(2, list))
    print(heapq.nsmallest(3, list))


    """
     make a max heap of tuples, and I would like to declare a custom comparator where it is sorted by the 
     first value of the tuple is descending order, and if the first value of the tuple is equal, 
     then sort by the 2nd value in descending order.
    """
    heap = []
    heapq.heappush(heap, CustomItem((2, 3)))
    heapq.heappush(heap, CustomItem((2, 4)))
    heapq.heappush(heap, CustomItem((2, 5)))
    heapq.heappush(heap, CustomItem((3, 1)))
    heapq.heappush(heap, CustomItem((5, 8)))

    while len(heap) != 0:
        print(heapq.heappop(heap).pair)



