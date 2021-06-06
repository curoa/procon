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


#XXX yield is slow
#XXX divmod is slow
"""
def yield_divisors(n):
    r = math.floor(math.sqrt(n))
    for i in range(1, n):
        if n % i == 0:
            yield i 
            yield a // i
"""

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]



if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))

    ans = yield_divisors(121)
    print('ans') # debug
    print(list(ans)) # debug



    print('\33[32m' + 'end' + '\033[0m') # debug

