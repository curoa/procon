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

def list_safe_get(l, index, default=None):
    if 0 < index < len(l):
        return l[index]
    return default

if __name__ == '__main__':
    l = [1, 2, 3]
    res = list_safe_get(l, 10)
    print('res') # debug
    print(res) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
