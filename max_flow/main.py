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

from collections import deque
class Dinic:

    def __init__(self, size):
        self.size = size
        self.pos = []
        self.graph = [[] for _ in range(size)]
        self.goal = None
        self.level = None
        self.used_edge = None

    def add_edge(self, frm, to, cap):
        self.pos.append((frm, len(self.graph[frm])))
        self.graph[frm].append([cap, to, len(self.graph[to])])
        self.graph[to].append([0, frm, len(self.graph[frm]) - 1])

    def bfs(self, start):
        level = [-1] * self.size
        level[start] = 0
        que = deque([start])
        while que:
            v = que.popleft()
            for cap, to, rev in self.graph[v]:
                if not cap > 0:
                    continue
                if level[to] >= 0:
                    continue
                level[to] = level[v] + 1
                que.append(to)
        self.level = level

    def dfs(self, v, flow):
        if v == self.goal:
            return flow
        for i in range(self.used_edge[v], len(self.graph[v])):
            self.used_edge[v] = i
            cap, to, rev = self.graph[v][i]
            if not cap > 0:
                continue
            if not self.level[v] < self.level[to]:
                continue
            sub_flow = self.dfs(to, min(flow, cap))
            if sub_flow > 0:
                self.graph[v][i][0] -= sub_flow
                self.graph[to][rev][0] += sub_flow
                return sub_flow
        return 0

    def max_flow(self, start, goal):
        self.goal = goal
        flow = 0
        while True:
            self.bfs(start)
            if self.level[self.goal] < 0:
                return flow
            self.used_edge = [0] * self.size
            f = self.dfs(start, math.inf)
            while f > 0:
                flow += f
                f = self.dfs(start, math.inf)

################################


# https://atcoder.jp/contests/typical90/tasks/typical90_an
# burn or bury problem
if __name__ == '__main__':
    n, w = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    c = []
    for i in range(n):
        tmp = list(map(lambda x: int(x) - 1, input().split()))
        tmp = tmp[1:]
        c.append(tmp)

    dinic = Dinic(n + 2)
    s = n
    t = n + 1
    for i in range(n):
        dinic.add_edge(s, i, a_list[i])
        dinic.add_edge(i, t, w)
        for j in c[i]:
            dinic.add_edge(j, i, math.inf)
    ans = sum(a_list) - dinic.max_flow(s, t)
    #print('ans') # debug
    print(ans)



    #print('\33[32m' + 'end' + '\033[0m') # debug

