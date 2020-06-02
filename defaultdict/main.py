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
from collections import defaultdict


if __name__ == '__main__':

    d = defaultdict(lambda: [])
    d['a'].append(9)
    d['b'].append(7)
    print('d') # debug
    print(d) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
