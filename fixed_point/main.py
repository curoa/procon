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

from decimal import Decimal

if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))

    f = 0.1
    v = f
    for _ in range(9):
        v += f
    print('v') # debug
    print(v) # debug

    d = Decimal("0.1")
    v = d
    for _ in range(9):
        v += d
    print('v') # debug
    print(v) # debug


    print('\33[32m' + 'end' + '\033[0m') # debug
