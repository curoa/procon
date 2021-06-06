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

from graph.main import Graph

# target: set of connected vertices
# return: target
def extract_connected(graph, v, target):
    if v in target:
        return target
    target.add(v)
    for to in graph.edges[v]:
        extract_connected(graph, to, target)
    return target

def get_sub_graph(graph, target):
    print("target", target) # debug
    new = Graph(len(target))
    converter = {}
    for i, v in enumerate(target):
        converter[v] = i
    for v in target:
        for to in graph.edges[v]:
            f = converter[v]
            t = converter[to]
            if f < t:
                new.add_edge(f, t)
    print("converter", converter) # debug
    print("new", new) # debug
    return new

# convert to list of connected graph
def disassembly(graph):
    l = []
    used = [False] * graph.size
    for v in range(graph.size):
        if used[v]:
            continue
        target = extract_connected(graph, v, set())
        g = get_sub_graph(graph, target)
        l.append(g)
        for u in target:
            used[u] = True
    return l



if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    graph = Graph(n)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph.add_edge(a, b)
    disassembly(graph)


    #print('\33[32m' + 'end' + '\033[0m') # debug

