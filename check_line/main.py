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

from itertools import combinations

################################

# for 2 dimensions
def calc_diff(p1, p2):
    d = [
            p1[0] - p2[0],
            p1[1] - p2[1],
            ]
    return d

def check_line(p1, p2, p3):
    d1 = calc_diff(p1, p2)
    d2 = calc_diff(p1, p3)
    if d1[1] * d2[0] == d1[0] * d2[1]:
        return True
    else:
        return False

################################

def solve(points):
    for a, b, c in combinations(range(len(points)), 3):
        if check_line(points[a], points[b], points[c]):
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    points = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        points.append((x, y))
    flg = solve(points)
    if flg:
        print("Yes")
    else:
        print("No")


    #print('\33[32m' + 'end' + '\033[0m') # debug

