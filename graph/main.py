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

    def __repr__(self):
        out = []
        out.append("vertices {}".format(self.vertices))
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
        self.vertices = [0] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = {}

    def __repr__(self):
        out = []
        out.append("vertices {}".format(self.vertices))
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
        self.vertices = [0] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = defaultdict(list)

    def __repr__(self):
        out = []
        out.append("vertices {}".format(self.vertices))
        for i, e in enumerate(self.edges):
            out.append("{} {}".format(i, pf(e)))
        return "\n".join(out)


    def add_edge(self, frm, to, weight):
        self.edges[frm][to].append(weight)

class AdjacentMatrix:

    def __init__(self, size):
        self.size = size
        self.matrix = make_2d_arr(size, size, math.inf)

    def __repr__(self):
        return pf(self.matrix)

    def add_edge(self, frm, to, cost):
        #self.matrix[frm][to] = cost
        self.update(frm, to, cost) # for multi edge

    def spread(self):
        for f in range(self.size):
            for t in range(self.size):
                self.transition(f, t)

    def transition(self, frm, to):
        cost = self.matrix[frm][to]
        for target in range(self.size):
            candidate_cost = self.matrix[target][frm] + cost
            self.update(target, to, candidate_cost)

    def update(self, frm, to, cost):
        self.matrix[frm][to] = min(self.matrix[frm][to], cost)

if __name__ == '__main__':
    data = int(input())
    data = list(map(int, input().split()))

    print('\33[32m' + 'end' + '\033[0m') # debug
