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
# Queue is very slow

# ref. https://ja.wikipedia.org/wiki/%E5%AE%8C%E5%85%A8%E9%A0%86%E5%88%97
def make_montmort_numbers(size, mod):
    montmort_numbers = [0] * (size + 1)
    signed_one = 1
    for i in range(2, len(montmort_numbers)):
        montmort_numbers[i] = i * montmort_numbers[i-1] % mod + signed_one
        montmort_numbers[i] %= mod
        signed_one *= -1
    return montmort_numbers

if __name__ == '__main__':

    mod = 10**9 + 7
    mn = make_montmort_numbers(7, mod)
    print('mn') # debug
    pp(mn) # debug
    print('mn[4]') # debug
    print(mn[4]) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug

