#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint as pp
from pprint import pformat as pf

import math
from sortedcontainers import SortedList, SortedDict, SortedSet
import bisect



# O(n log n)
def solve(seq):
    dp = [math.inf] * (len(seq) + 1)
    dp[0] = -1 * math.inf
    for value in seq:
        key = bisect.bisect_left(dp, value)
        dp[key] = value
        print('dp') # debug
        print(dp) # debug
    key = bisect.bisect_left(dp, math.inf)
    return key - 1


if __name__ == '__main__':
    data = list(map(int, input().split()))

    print('data') # debug
    print(data) # debug
    ans = solve(data)
    print('ans') # debug
    print(ans) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
