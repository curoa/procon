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

def rev_range(m):
    i = m
    while i >= 0:
        yield m
        i -= 1

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
# Queue is very slow
from collections import defaultdict

def make_2d_arr(s1, s2, default=0):
    a = [None] * s1
    for i, _ in enumerate(a):
        a[i] = [default] * s2
    return a

def solve(n, k):
    #TODO you can copy this func.  but edit dp and handling it's value.
    n = list(map(int, str(n)))
    ceil_value = 1 #TODO edit
    dp = defaultdict(int) # dp[value] = count #TODO edit
    for i, d in enumerate(n):
        ndp = defaultdict(int) #TODO edit
        # pick freely
        for value, count in dp.items():
            for pick_v in range(10):
                ndp[value * pick_v] += count #TODO edit
        # pick carefully
        for pick_v in range(d):
            if i == 0 and pick_v == 0:
                continue
            ndp[ceil_value * pick_v] += 1 #TODO edit
        ceil_value *= d
        # pick first digit 
        if i != 0:
            for pick_v in range(1, 9 + 1):
                #print('first pick_v', pick_v) # debug
                ndp[pick_v] += 1 #TODO edit
        dp = ndp
        #print('dp', dp) # debug
    ans = 0 # calc ans
    return ans




# https://atcoder.jp/contests/abc208/tasks/abc208_e
if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    ans = solve(n, k)
    #print('ans') # debug
    print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug

