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


class Queue:

    def __init__(self):
        self.data = []
        self.sub = []
        self.pos = 0
        self.max = 2

    def put(self, value):
        if len(self.data) < self.max:
            self.data.append(value)
        else:
            self.sub.append(value)

    def pop(self):
        value = self.data[self.pos]
        self.pos += 1
        if self.pos >= len(self.data):
            self.data = self.sub
            self.sub = []
            self.max = 2 ** (len(bin(len(self.data))) - 2)
            self.pos = 0
        return value

    def is_empty(self):
        if len(self.data) == 0 and len(self.sub) == 0:
            return True
        return False

if __name__ == '__main__':
    pass

