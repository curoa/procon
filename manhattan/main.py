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
from collections import defaultdict

def right_projection(x, y):
    return x + y

def left_projection(x, y):
    return y - x

def manhattan1(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def manhattan2(p1, p2):
    right_diff = abs(right_projection(p1[0], p1[1]) - right_projection(p2[0], p2[1]))
    left_diff = abs(left_projection(p1[0], p1[1]) - left_projection(p2[0], p2[1]))
    return max(right_diff, left_diff)


if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))

    import random
    for _ in range(100):
        x1 = random.randrange(1, 100)
        y1 = random.randrange(1, 100)
        x2 = random.randrange(1, 100)
        y2 = random.randrange(1, 100)
        d1 = manhattan1([x1, y1], [x2, y2])
        d2 = manhattan2([x1, y1], [x2, y2])
        assert (d1 == d2)


    print('\33[32m' + 'end' + '\033[0m') # debug

