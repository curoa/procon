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

def rev_renge(m):
    i = m
    while i >= 0:
        yield m
        i -= 1

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
# Queue is very slow
from collections import defaultdict


# decimal: how accurate input float; e.g. 0.1234 then 4
def load(s, decimal):
    tmp = s.split(".")
    if len(tmp) == 1:
        return int(tmp[0]) * scale
    i, f = tmp
    v = int(i) * scale
    f = f + "0" * (decimal - len(f))
    v += int(f)
    print("s, f, v", s, f, v) # debug
    return v


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    s = input().strip()
    query = list(input().split())

    print('\33[32m' + 'end' + '\033[0m') # debug

