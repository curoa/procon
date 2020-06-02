#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect

from heapq import heappush, heappop
class PriorityQueue:

    def __init__(self):
        self.contaier = []

    def push(self, priority, value): # smaller is first
        heappush(self.contaier, (priority, value))

    def pop(self):
        return heappop(self.contaier)

    def is_empty(self):
        return len(self.contaier) == 0


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
