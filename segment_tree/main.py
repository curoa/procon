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

class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2-1) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size-1
        self.dat[i] = x
        while i > 0:
            i = (i-1) >> 1
            self.dat[i] = self.f(self.dat[i*2+1], self.dat[i*2+2])

    def query(self, l, r, k=0, L=0, R=None):
        if R is None:
            R = self.size
        if R <= l or r <= L:
            return self.default
        if l <= L and R <= r:
            return self.dat[k]
        else:
            lres = self.query(l, r, k*2+1, L, (L+R) >> 1)
            rres = self.query(l, r, k*2+2, (L+R) >> 1, R)
            return self.f(lres, rres)

if __name__ == '__main__':

    # get interval sum
    st = SegmentTree(6)
    for i in range(6):
        st.update(i, i)
    a = st.query(3, 6)
    print('a', a) # debug

    # get min
    f = lambda x, y : min(x, y)
    st = SegmentTree(6, f, math.inf)
    for i in range(6):
        st.update(i, 10 - i)
    a = st.query(2, 3)
    print('st.dat') # debug
    print(st.dat) # debug
    print('a', a) # debug


    print('\33[32m' + 'end' + '\033[0m') # debug
