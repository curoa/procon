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

def point_add(p1, p2):
    x = p1[0] + p2[0]
    y = p1[1] + p2[1]
    return (x, y)

def point_diff(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return (x, y)

# return value: if value > 0 then counter-clockwise (`p1` to `p2`)
def cross_product(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def cross_product_with_base(p1, p2, pb):
    return cross_product(point_diff(p1, pb), point_diff(p2, pb))

def check_line(p1, p2, p3):
    d1 = point_diff(p1, p2)
    d2 = point_diff(p1, p3)
    if d1[1] * d2[0] == d1[0] * d2[1]:
        return True
    else:
        return False

def calc_area(p1, p2, p3):
    d1 = point_diff(p1, p2)
    d2 = point_diff(p1, p3)
    return abs(d1[1] * d2[0] - d1[0] * d2[1]) / 2


def get_convex(points):
    points.sort()
    fly = [points[0], points[1]]
    dive = [points[0], points[1]]
    for p in points[2:]:
        while len(fly) >= 2 and cross_product_with_base(p, fly[-1], fly[-2]) >= 0:
            fly.pop()
        fly.append(p)
        while len(dive) >= 2 and cross_product_with_base(p, dive[-1], dive[-2]) <= 0:
            dive.pop()
        dive.append(p)
    convex = fly[:-1] + list(reversed(dive))
    convex.pop()
    return convex

# exclude `f` and `t`
def count_lattice_point_on_edge(f, t):
    x, y = point_diff(f, t)
    return math.gcd(abs(x), abs(y)) - 1

def count_edge_point(convex):
    count = len(convex)
    n = len(convex)
    convex.append(convex[0]) # add guard
    for i in range(len(convex) - 1):
        f = convex[i]
        t = convex[i+1]
        count += count_lattice_point_on_edge(f, t)
    convex.pop() # remove guard
    return count

def calc_area_of_polygon(convex):
    area = 0
    convex.append(convex[0]) # add guard
    for i in range(len(convex) - 1):
        f = convex[i]
        t = convex[i+1]
        area += (t[0] - f[0]) * (t[1] + f[1])
    convex.pop() # remove guard
    area = abs(area)
    #return area / 2 # correct area
    return area # useful to avoid calc-error


# pick's theorem: https://ja.wikipedia.org/wiki/%E3%83%94%E3%83%83%E3%82%AF%E3%81%AE%E5%AE%9A%E7%90%86
################################

def solve(points):
    for a, b, c in combinations(range(len(points)), 3):
        if check_line(points[a], points[b], points[c]):
            return True
    return False

# ref. https://atcoder.jp/contests/typical90/tasks/typical90_ao
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

