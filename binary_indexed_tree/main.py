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


class BIT: # binary indexed tree
    """
    http://hos.ac/slides/20140319_bit.pdf
    """

    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1) # var[0] is dummy

    def add(self, pos, val):
        assert(pos > 0)
        k = pos
        while k <= self.size:
            self.data[k] += val
            # for next
            k += k & -k

    def sum(self, pos):
        assert(pos > 0)
        s = 0
        k = pos
        while k > 0:
            s += self.data[k]
            # for next
            k -= k & -k
        return s


if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))
    bit = BIT(8)
    for i in range(8):
        bit.add(i, i)
        a = bit.sum(i)
        print('a') # debug
        print(a) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug

"""
int N;
int bit[1000010];
void add(int a, int w) {
for (int x = a; x <= N; x += x & -x) bit[x] += w;
}
int sum(int a) {
 int ret = 0;
for (int x = a; x > 0; x -= x & -x) ret += bit[x];
 return ret;
}
"""

""" 0 starts
// v[a] += w
void add(int a, int w) {
for (int x = a; x < N; x |= x + 1) {
 bit[x] += w;
}
}

// v[0] + ... + v[a - 1]
int sum(int a) {
 int ret = 0;
for (int x = a - 1; x >= 0; x = (x & (x + 1)) - 1) {
 ret += bit[x];
}
 return ret;
}
"""
