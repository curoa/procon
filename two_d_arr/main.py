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

def make_2d_arr(s1, s2, default=0):
    a = [None] * s1
    for i, _ in enumerate(a):
        a[i] = [default] * s2
    return a


if __name__ == '__main__':
    a = make_2d_arr(3, 8, -1)
    print('a') # debug
    pp(a) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
