#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

def ternary_op(flg, a, b):
    if flg:
        return a
    else:
        return b

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
# Queue is very slow
from collections import defaultdict

################################

# ref. https://tsubo.hatenablog.jp/entry/2020/06/15/124657
import heapq
class HeapDict:

    def __init__(self, flg_min):
        self.h = []
        self.d = dict()
        self.flg_min = flg_min

    def __repr__(self):
        out = ""
        out += pf(self.h)
        out += pf(self.d)
        return out

    def insert(self, x):
        x = self.convert(x)
        heapq.heappush(self.h, x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self, x):
        x = self.convert(x)
        if x not in self.d or self.d[x] == 0:
            raise RuntimeError(f"{x} is not in HeapDict")
        else:
            self.d[x] -= 1
        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self, x):
        x = self.convert(x)
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self):
        if self.flg_min:
            return self.h[0]
        else:
            raise RuntimeError("flg_min is False, but get_min called.")

    def get_max(self):
        if self.flg_min is False:
            return -1 * self.h[0]
        else:
            raise RuntimeError("flg_min is True, but get_max called.")

    def is_empty(self):
        if len(self.h) == 0:
            return True
        else:
            return False

    def convert(self, x):
        if self.flg_min is False:
            x = -1 * x
        return x

################################

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    s = input().strip()
    query = list(input().split())

    print('\33[32m' + 'end' + '\033[0m') # debug

