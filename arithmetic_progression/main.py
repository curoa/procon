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


# first: first number
# last: last number
# n: number of items
def arithmetic_progression_sum_1(first, last, n):
    return n * (first + last) / 2 # return float

# a: first number
# d: diff
# n: number of items
def arithmetic_progression_sum_2(a, d, n):
    return n / 2 * (2 * a + (n - 1) * d) # return float


if __name__ == '__main__':
    print('arithmetic_progression_sum_1(100, 30, 7)') # debug
    print(arithmetic_progression_sum_1(100, 30, 7)) # debug
    print('arithmetic_progression_sum_2(-5, 3, 10)') # debug
    print(arithmetic_progression_sum_2(-5, 3, 10)) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug

