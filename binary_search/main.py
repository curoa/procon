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

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
# Queue is very slow
from collections import defaultdict


# return: index, target_list[index] == want
def binary_search(want, target_list):
    l = 0 # include l
    r = len(target_list) # exclude r
    while l < r:
        mid = l + (r - l) // 2 # l <= mid < r
        v = target_list[mid]
        if want < v:
            r = mid
        elif v < want:
            l = mid + 1 # not hit by mid
        else: # v == want
            return mid
    return None

# threshold is int between l and r 
def binary_search(want, target_list):
    l = -1 # l does not store answer
    r = len(target_list) # exclude r
    while l + 1 < r:
        mid = l + (r - l) // 2 # l <= mid < r
        v = target_list[mid]
        if want < v:
            r = mid
        elif v < want:
            l = mid # l does not store answer
        else: # v == want
            return mid
    return l,, r



if __name__ == '__main__':
    #n = int(input())
    #data = list(map(int, input().split()))
    #s = input().strip()
    #query = list(input().split())

    target_list = [1, 3, 5]
    print('target_list') # debug
    print(target_list) # debug
    for want in [0, 1, 2, 3, 4, 5, 6]:
        i = binary_search(want, target_list)
        print("want, i", want, i) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug

