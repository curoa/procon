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

def rev_renge(m):
    i = m
    while i >= 0:
        yield m
        i -= 1

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
# Queue is very slow
from collections import defaultdict

################################

def make_2d_arr(s1, s2, default=0):
    a = [None] * s1
    for i, _ in enumerate(a):
        a[i] = [default] * s2
    return a

def matrix_inner_product(x, y):
    z = make_2d_arr(len(x), len(y[0]))
    for i, _z in enumerate(z):
        for j in range(len(_z)):
            v = 0
            for k in range(len(x[i])):
                v += x[i][k] * y[k][j]
                v %= MOD
            z[i][j] = v
    return z

def fib_prepare(size):
    matrix = [
            [1, 1],
            [1, 0],
            ]
    p = [matrix]
    for i in range(size.bit_length()):
        m = p[-1]
        new = matrix_inner_product(m, m)
        p.append(new)
    #print('p') # debug
    #pp(p) # debug
    return p

# p: power of matrix made by fib_prepare
def fib(i, p):
    v = [
            [1, 0],
            [0, 1],
            ]
    b = 0
    #print("bin(i)", bin(i)) # debug
    while i > 0:
        flg = i & 1
        if flg:
            v = matrix_inner_product(v, p[b])
        i = i >> 1
        b += 1
    return v[0][0]

################################

if __name__ == '__main__':
    MOD = 998244353
    size = 20
    p = fib_prepare(20)
    for i in range(size):
        v = fib(i, p)
        print("v", v) # debug

    #print('\33[32m' + 'end' + '\033[0m') # debug

