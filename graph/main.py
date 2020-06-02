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

class Graph:

    def __init__(self, size):
        # id starts from 0
        self.size = size
        self.vertices = [0] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = []

    def add_edge(self, frm, to):
        self.edges[frm].append(to)
        self.edges[to].append(frm)

if __name__ == '__main__':
    data = int(input())
    data = list(map(int, input().split()))

    print('\33[32m' + 'end' + '\033[0m') # debug
