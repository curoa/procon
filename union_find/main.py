#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import pysnooper # @pysnooper.snoop()
from pprint import pprint as pp
from pprint import pformat as pf


################################

# id starts from 0
class UnionFind:

    def __init__(self, size):
        self.group = list(range(size))
        self.count_group = len(self.group)

    def __repr__(self):
        return pf(self.count_group) + pf(self.group)

    def find(self, member):
        if member == self.group[member]:
            return member
        else:
            g = self.find(self.group[member])
            self.group[member] = g
            return g

    def union(self, a, b):
        ga = self.find(a)
        gb = self.find(b)
        if ga == gb:
            return
        self.group[gb] = ga
        self.count_group -= 1

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def same_all(self):
        return self.count_group == 1

################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser('This is hogehoge')
    args = parser.parse_args()

    uf = UnionFind(10)
    for i in range(0, 10, 2):
        uf.union(i+1, i)
    for i in range(10):
        r = uf.find(i)
        print('r', r) # debug
    for i in range(9):
        r = uf.same(i, i+1)
        print('r', r) # debug
    print('uf.group') # debug
    print(uf.group) # debug

    print('\33[32m' + 'end' + '\033[0m')
