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

def convert(key):
    magic = 26 # number of alphabet
    return chr(ord("a") + (key % magic) - 1)

def str_reverse(s):
    return "".join(list(reversed(s)))


if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))

    print('convert(3)') # debug
    print(convert(3)) # debug
    print('str_reverse("abc")') # debug
    print(str_reverse("abc")) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug

