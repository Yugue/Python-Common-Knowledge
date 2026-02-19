from sortedcontainers import SortedList, SortedSet, SortedDict


# =========================================================
# 1. SORTEDLIST
# =========================================================
"""
Stores values in sorted order.
Duplicates allowed.
"""

sl = SortedList([5, 1, 3])
print(sl)  # [1, 3, 5]

# ---- Common Methods ----
sl.add(4)                 # O(log n)
sl.remove(3)              # O(log n)
sl.discard(10)            # O(log n), no error if missing
sl.pop()                  # O(log n), remove largest by default
sl.pop(0)                 # O(log n), remove smallest
sl.clear()                # O(n)

# ---- Access ----
sl[0]                     # O(1) smallest
sl[-1]                    # O(1) largest
len(sl)                   # O(1)

# ---- Binary Search ----
sl.bisect_left(4)         # O(log n), first index >= 4
sl.bisect_right(4)        # O(log n), first index > 4

# ---- Range Count ----
count = sl.bisect_right(5) - sl.bisect_left(2)  # O(log n)

"""
Properties:
- Always sorted
- Fast insert/delete
- Supports indexing
"""


# =========================================================
# 2. SORTEDSET
# =========================================================
"""
Stores unique values in sorted order.
No duplicates.
"""

ss = SortedSet([5, 1, 3])
print(ss)  # SortedSet([1, 3, 5])

# ---- Common Methods ----
ss.add(4)                 # O(log n)
ss.remove(3)              # O(log n)
ss.discard(10)            # O(log n)
ss.pop()                  # O(log n), remove largest
ss.pop(0)                 # O(log n), remove smallest
ss.clear()                # O(n)

# ---- Access ----
ss[0]                     # O(1)
ss[-1]                    # O(1)
4 in ss                   # O(log n)

# ---- Binary Search ----
ss.bisect_left(4)         # O(log n)
ss.bisect_right(4)        # O(log n)

"""
Properties:
- Always sorted
- Unique elements
- Fast predecessor/successor
"""


# =========================================================
# 3. SORTEDDICT
# =========================================================
"""
Dictionary sorted by key.
"""

sd = SortedDict({5: "A", 1: "B", 3: "C"})
print(sd)  # SortedDict({1: 'B', 3: 'C', 5: 'A'})

# ---- Insert / Update ----
sd[4] = "D"               # O(log n)

# ---- Remove ----
del sd[3]                 # O(log n)
sd.pop(4)                 # O(log n)

# ---- Lookup ----
sd[5]                     # O(1) average
5 in sd                   # O(1) average

# ---- Smallest / Largest ----
sd.peekitem(0)            # O(log n), smallest (key, value)
sd.peekitem(-1)           # O(log n), largest (key, value)

# ---- Binary Search on Keys ----
sd.bisect_left(4)         # O(log n)
sd.bisect_right(4)        # O(log n)

# ---- Range Iteration ----
for key in sd.irange(2, 6):  # O(log n + k)
    print(key, sd[key])

"""
Properties:
- Keys always sorted
- O(log n) insert/delete
- O(1) key lookup
- Efficient range queries
"""


# =========================================================
# COMPLEXITY SUMMARY
# =========================================================
"""
SortedList:
    add/remove      -> O(log n)
    index access    -> O(1)
    bisect          -> O(log n)

SortedSet:
    add/remove      -> O(log n)
    membership      -> O(log n)
    index access    -> O(1)

SortedDict:
    insert/delete   -> O(log n)
    key lookup      -> O(1) avg
    peek smallest   -> O(log n)
    bisect          -> O(log n)
"""
