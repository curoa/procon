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
        #self.vertices = [0] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = []

    def __repr__(self):
        out = []
        #out.append("vertices {}".format(self.vertices))
        for i, e in enumerate(self.edges):
            out.append("{}{}".format(i, pf(e)))
        return "\n".join(out)

    def add_edge(self, frm, to):
        self.edges[frm].append(to)
        self.edges[to].append(frm)

class WeightedGraph:

    def __init__(self, size):
        # id starts from 0
        self.size = size
        #self.vertices = [0] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = {}

    def __repr__(self):
        out = []
        #out.append("vertices {}".format(self.vertices))
        for i, e in enumerate(self.edges):
            out.append("{}{}".format(i, pf(e)))
        return "\n".join(out)


    def add_edge(self, frm, to, weight):
        self.edges[frm][to] = weight
        self.edges[to][frm] = weight

# allow loop edge
class WeightedDirectedMultiEdgeGraph:

    def __init__(self, size):
        # id starts from 0
        self.size = size
        #self.vertices = [0] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = defaultdict(list)

    def __repr__(self):
        out = []
        #out.append("vertices {}".format(self.vertices))
        for i, e in enumerate(self.edges):
            out.append("{} {}".format(i, pf(e)))
        return "\n".join(out)


    def add_edge(self, frm, to, weight):
        self.edges[frm][to].append(weight)
        #self.edges[to][frm].append(weight)

class AdjacentMatrix:

    def __init__(self, size):
        self.size = size
        self.matrix = make_2d_arr(size, size, math.inf)
        for i in range(self.size):
            self.matrix[i][i] = 0

    def __repr__(self):
        return pf(self.matrix)

    def add_edge(self, frm, to, cost):
        #self.matrix[frm][to] = cost
        self.update(frm, to, cost) # for multi edge

    # ref. https://qiita.com/okaryo/items/8e6cd73f8a676b7a5d75
    # O(size^3)
    def warshall_floyd(self):
        for k in range(self.size): # via
            for f in range(self.size):
                for t in range(self.size):
                    cost = self.matrix[f][k] + self.matrix[k][t]
                    self.update(f, t, cost)

    def update(self, frm, to, cost):
        self.matrix[frm][to] = min(self.matrix[frm][to], cost)

if __name__ == '__main__':
    data = int(input())
    data = list(map(int, input().split()))

    print('\33[32m' + 'end' + '\033[0m') # debug
