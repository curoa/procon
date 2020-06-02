#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint as pp
from pprint import pformat as pf

import math
from sortedcontainers import SortedList, SortedDict, SortedSet


if __name__ == '__main__':
    data = int(input())
    data = list(map(int, input().split()))

    sl = SortedList([3, 4, 1])
    print('sl') # debug
    print(sl) # debug



    print('\33[32m' + 'end' + '\033[0m')
