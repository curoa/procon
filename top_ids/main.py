#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect

from procon.priority_queue.main import PriorityQueue
class HeapedSet:

    def __init__(self):
        self.que = PriorityQueue()
        self.id_set = set()

    def add(self, id_, value):
        self.que.push(value, id_)
        self.id_set.add(id_)

    def delete(self, id_):
        self.id_set.discard(id_)

    def bottom(self):
        while True:
            value, id_ = self.que.min()
            if value is None:
                return None, None
            if id_ in self.id_set:
                break
            self.que.pop()
        return id_, value


if __name__ == '__main__':
    hs = HeapedSet()
    n = int(input())
    for _ in range(n):
        id_, value = list(map(int, input().split()))
        hs.add(id_, value)
        ans = hs.bottom()
        print('ans', ans) # debug
    dels = list(map(int, input().split()))
    for d in dels:
        hs.delete(d)
        ans = hs.bottom()
        print('ans', ans) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
