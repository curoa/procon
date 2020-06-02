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


class ModInt(int):

    MOD = None

    def __add__(self, other):
        self = ModInt(int.__add__(self, other) % ModInt.MOD)
        return self

    def __mul__(self, other):
        self = ModInt(int.__mul__(self, other) % ModInt.MOD)
        return self


if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))

    ModInt.MOD = 5
    i = ModInt(2)
    i = i + 9
    i = i * 2
    i += 15
    i *= 2
    print('i') # debug
    print(i) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
