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


def make_power(base, size, mod):
    result = [1] * (size + 1)
    for i in range(1, size + 1):
        result[i] = result[i-1] * base % mod
    return result


if __name__ == '__main__':

    mod = 10**9+7
    pow11 = make_power(11, 3, mod)
    print('pow11') # debug
    pp(pow11) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug

