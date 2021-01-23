#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

handler = logging.FileHandler(filename="log")
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(message)s'))
logger = logging.getLogger(__name__)
logger.addHandler(handler)

#logger.warn('hello warn')
#logger.error('hello error')
#logger.info('hello info')
#logger.debug('hello debug')


import argparse
import pysnooper # @pysnooper.snoop()
from pprint import pprint as pp
from pprint import pformat as pf
import math

def factorial(n, mod=None, memo=False):
    if memo:
        factorial.memo = [1] * (n + 1)
        for i in range(1, n + 1):
            print('i', i) # debug
            if mod is None:
                factorial.memo[i] = i * factorial.memo[i - 1]
            else:
                factorial.memo[i] = i * factorial.memo[i - 1] % mod
            print('factorial.memo[i]', factorial.memo[i]) # debug
            print() # debug
    return factorial.memo[n]

# if `mod` works in factorial() then choose() fails
def choose(n, r, mod=None):
    a = factorial(n)
    b = factorial(r)
    c = factorial(n - r)
    if mod is None:
        res = a // b // c
    else:
        # fermat's little theorem
        res = a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod) % mod
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser('This is hogehoge')
    args = parser.parse_args()

    mod = 998244353
    n = 65234
    a = factorial(n, mod, True)
    a = factorial(n, mod)
    print('factorial.memo') # debug
    print(factorial.memo) # debug
    assert math.factorial(n) % mod == factorial(n), 'hoge'
    for i in range(5 + 1):
        a = choose(10, i)
        print(a) # debug

    print('\33[32m' + 'end' + '\033[0m')

