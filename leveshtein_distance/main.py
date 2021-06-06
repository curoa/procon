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

#ref. https://takuti.me/ja/note/levenshtein-distance/
def levenshtein(s1, s2):
    """
    >>> levenshtein('kitten', 'sitting')
    3
    >>> levenshtein('あいうえお', 'あいうえお')
    0
    >>> levenshtein('あいうえお', 'かきくけこ')
    5
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement
    return dp[n][m]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    ans = levenshtein(al, bl)
    #print('ans') # debug
    print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug

