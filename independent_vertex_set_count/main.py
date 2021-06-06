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


# use global: counts
# use global: not_connected: 
# yet: bit set of yet determined
# this is fast enough for 72 vertex
def independent_set_count(yet):
    if yet in counts:
        return counts[yet]
    youngest = yet & -1 * yet
    not_me = yet ^ youngest
    yes_me = yet & not_connected[youngest.bit_length() - 1]
    #print("yet", bin(yet)[2:]) # debug
    #print("not_me", bin(not_me)[2:]) # debug
    #print("yes_me", bin(yes_me)[2:]) # debug
    counts[yet] = independent_set_count(not_me) + independent_set_count(yes_me)
    return counts[yet]



if __name__ == '__main__':
    n = 3
    not_connected = [ # graph size 3 e 0 2
            int("010", 2),
            int("101", 2),
            int("010", 2),
            ]
    #print("not_connected", not_connected) # debug
    counts = {0: 1}
    ans = independent_set_count((1 << n) - 1)
    #print('ans') # debug
    print(ans)


    print('\33[32m' + 'end' + '\033[0m') # debug

