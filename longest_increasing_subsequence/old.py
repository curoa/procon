#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pprint import pprint as pp
from pprint import pformat as pf

import math
from first_over import first_over_or_same

class SolverLIS:
    """
    solver = SolverLIS(data)
    ans = solver.run()
    """

    def __init__(self, seq):
        self.seq = seq #TODO assert: element > 0
        self.dp = [math.inf] * (len(seq) + 1) # var[length] = min value
        self.dp[0] = 0

    def run(self):
        for i, value in enumerate(self.seq):
            self.use(value, i)
        return self.get_longest_increasing_subsequence_size()

    def use(self, value):
        key, over_value = first_over_or_same(self.dp, value)
        if key is not None:
            self.dp[key] = value

    def get_longest_increasing_subsequence_size(self):
        length = len(self.dp) - 1
        while length >= 0:
            value = self.dp[length]
            if value is not math.inf and value > 0:
                return length
            # for next
            length -= 1
        return 0


if __name__ == '__main__':
    for _ in range(4):
        data = list(map(int, input().split()))
        print('data') # debug
        print(data) # debug
        solver = SolverLIS(data)
        ans = solver.run()
        print('ans') # debug
        print(ans) # debug

    print('\33[32m' + 'end' + '\033[0m')
