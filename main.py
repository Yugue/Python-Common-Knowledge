import time
from collections import defaultdict, deque
from functools import cmp_to_key, lru_cache
import math
from math import ceil, sqrt, floor
import random
from abc import ABC, abstractmethod
from typing import Optional
import copy
import requests
import time
from datetime import datetime, timedelta
import heapq
import requests


class Solution:
    def is_prime(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def nonSpecialCount(self, l: int, r: int) -> int:
        ans = r - l + 1
        for sqrt_num in range(ceil(sqrt(l)), floor(sqrt(r)) + 1):
            if self.is_prime(sqrt_num):
                ans -= 1
        return ans


if __name__ == '__main__':
    print(-2 % 2)

