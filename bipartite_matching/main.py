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

# ref. https://manabitimes.jp/math/1147
class BipartiteMatching:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.edges = [None] * n
        for i in range(n):
            self.edges[i] = []

    def add_edge(self, frm, to):
        self.edges[frm].append(to)

    def match(self):
        n, m, edges = self.n, self.m, self.edges
        pre = [-1] * n
        root = [-1] * n
        p = [-1] * n
        q = [-1] * m
        flg_update = True
        while flg_update:
            flg_update = False
            s = [] # not matched vertex list
            s_i = 0
            for i in range(n):
                if p[i] == -1:
                    root[i] = i
                    s.append(i)
            while s_i < len(s):
                v = s[s_i]
                s_i += 1
                if p[root[v]] != -1:
                    continue
                for u in edges[v]:
                    if q[u] == -1:
                        # update to increasing path
                        while u != -1:
                            q[u] = v
                            p[v], u = u, p[v]
                            v = pre[v]
                        flg_update = True
                        break
                    # memo increasing path candidate
                    u = q[u]
                    if pre[u] == -1:
                        pre[u] = v
                        root[u] = root[v]
                        s.append(u)
            if flg_update:
                for i in range(n):
                    pre[i] = -1
                    root[i] = -1
        return p


################################

directions = {
        (+1, +0): 1,
        (+1, +1): 2,
        (+0, +1): 3,
        (-1, +1): 4,
        (-1, +0): 5,
        (-1, -1): 6,
        (+0, -1): 7,
        (+1, -1): 8,
        }


def to_graph():
    target = {}
    for i, xy in enumerate(second):
        target[xy] = i
    #print('target') # debug
    #pp(target) # debug
    for v, (x, y) in enumerate(first):
        for dx, dy in directions:
            tx = x + t * dx
            ty = y + t * dy
            tpl = (tx, ty)
            if tpl in target:
                to = target[tpl]
                #print("v, to", v, to) # debug
                bm.add_edge(v, to)
    #print('dinic.graph') # debug
    #pp(dinic.graph) # debug

def get_direction(v, to):
    fx, fy = first[v]
    sx, sy = second[to]
    #print("fx, fy", fx, fy) # debug
    #print("sx, sy", sx, sy) # debug
    if fx + t == sx and fy + 0 == sy:
        return 1
    if fx + t == sx and fy + t == sy:
        return 2
    if fx + 0 == sx and fy + t == sy:
        return 3
    if fx - t == sx and fy + t == sy:
        return 4
    if fx - t == sx and fy + 0 == sy:
        return 5
    if fx - t == sx and fy - t == sy:
        return 6
    if fx + 0 == sx and fy - t == sy:
        return 7
    if fx + t == sx and fy - t == sy:
        return 8
    """
    dx = sx - fx
    dy = sy - fy
    if dx != 0: dx = dx // abs(dx)
    if dy != 0: dy = dy // abs(dy)
    #print("dx, dy", dx, dy) # debug
    return directions[(dx, dy)]
    """

def solve():
    to_graph()
    #print("start, end", start, end) # debug
    matching = bm.match()
    if min(matching) == -1:
        return False, None
    ans_list = [None] * n
    for v in range(n):
        to = matching[v]
        ans_list[v] = get_direction(v, to)
    #print("ans_list", ans_list) # debug
    return True, ans_list




if __name__ == '__main__':
    n, t = list(map(int, input().split()))
    bm = BipartiteMatching(n, n)
    first = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        first.append((x, y))
    second = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        second.append((x, y))
    ans, ans_list = solve()
    if ans:
        print("Yes")
        out = " ".join(map(str, ans_list))
        print(out)
    else:
        print("No")


    #print('\33[32m' + 'end' + '\033[0m') # debug

