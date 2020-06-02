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


def mutual_division_method(a, b):
    while not (a == 0 or b == 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a




if __name__ == '__main__':
    ans = mutual_division_method(32, 6)
    print('ans') # debug
    print(ans) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
