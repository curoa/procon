#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect

class Counter(dict):
    def __missing__(self, key):
        self[key] = 0
        return self[key]


if __name__ == '__main__':


    d = Counter()
    d[9] += 1
    print('d') # debug
    print(d) # debug


    print('\33[32m' + 'end' + '\033[0m') # debug
