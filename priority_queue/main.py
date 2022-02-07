#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect


################################

class PrioritizedItem:

    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __lt__(a, b):
        return a.priority < b.priority

    def __repr__(self):
        return "({}) {}".format(self.priority, self.item)

from heapq import heappush, heappop
class PriorityQueue:

    def __init__(self, flg_min):
        self.contaier = []
        self.flg_min = flg_min # if max then False

    def __repr__(self):
        #return pf(self.contaier)
        return pf(sorted(self.contaier))

    def push(self, priority, value):
        if not self.flg_min:
            priority = -1 * priority
        heappush(self.contaier, PrioritizedItem(priority, value))

    def pop(self):
        pi = heappop(self.contaier)
        if self.flg_min:
            return pi.priority, pi.item
        else:
            return -1 * pi.priority, pi.item


    def min(self):
        if not self.flg_min:
            raise RuntimeError("min() of PriorityQueue for max called")
        return self.top()

    def max(self):
        if self.flg_min:
            raise RuntimeError("max() of PriorityQueue for min called")
        return self.top()

    def top(self):
        if self.is_empty():
            return None
        return self.contaier[0].item

    def is_empty(self):
        return len(self.contaier) == 0

################################


if __name__ == '__main__':
    data = list(map(int, input().split()))

    pq = PriorityQueue()
    for d in data:
        pq.push(d, d)
    while not pq.is_empty():
        d = pq.pop()
        print('d') # debug
        print(d) # debug


    print('\33[32m' + 'end' + '\033[0m') # debug
