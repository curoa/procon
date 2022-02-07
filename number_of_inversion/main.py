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

from procon.binary_indexed_tree.main import BIT

# O(n log n)
# ref. https://scrapbox.io/pocala-kyopro/%E8%BB%A2%E5%80%92%E6%95%B0
# number of swap to reorder
class NumberOfInversion:

    def __init__(self, data):
        #assert(sorted(data) == list(range(len(data)))) # debug
        self.data = data
        self.bit = BIT(len(data))

    def solve(self):
        count = 0
        for v in self.data:
            v += 1 # BIT[0] is dummy
            count += self.bit.sum() - self.bit.sum(v)
            self.bit.add(v, 1)
        return count


if __name__ == '__main__':

    d = [3, 2, 1, 0]
    print('d') # debug
    print(d) # debug
    ans = NumberOfInversion(d).solve()
    #print('ans') # debug
    print(ans)


    #print('\33[32m' + 'end' + '\033[0m') # debug

