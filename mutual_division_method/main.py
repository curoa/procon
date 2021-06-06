#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect


# ref. http://fuee.u-fukui.ac.jp/~hirose/lectures/crypto_security/slides/01number_algebra.pdf


from math import gcd # O(log n)

# ref. https://tex2e.github.io/blog/crypto/modular-mul-inverse
# Extended Euclidean Algorithm
# a*x + b*y = gcd(a, b)
def extgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0 # `a` is gcd(a, b)

def modinv(a, m):
    g, x, y = extgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def lcm(a, b): # least common multiple
    return a * b // gcd(a, b)

def all_lcm(l):
    hand = 1
    for v in l:
        hand = lcm(hand, v)
    return hand

if __name__ == '__main__':
    ans = gcd(32, 12)
    print('ans') # debug
    print(ans) # debug
    ans = gcd(0, 12)
    print('ans') # debug
    print(ans) # debug

    print("a, x, y", a, x, y) # debug



    print('\33[32m' + 'end' + '\033[0m') # debug
