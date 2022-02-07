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

directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        ]

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    s = input().strip()
    query = list(input().split())

    print('\33[32m' + 'end' + '\033[0m') # debug

