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

################################

# you can use math.factorial
# ref. https://algo-logic.info/combination/#toc_id_2_3
# assert mod is prime, n is smaller than mod
class Magician:

    def __init__(self, n, mod):
        size = n + 1
        fac = [0] * size # factorial
        inv = [0] * size
        finv = [0] * size
        fac[:2] = 1, 1
        inv[1] = 1
        finv[:2] = 1, 1
        for i in range(2, size):
            fac[i] = fac[i-1] * i % mod
            inv[i] = -1 * inv[mod%i] * (mod // i) % mod
            finv[i] = finv[i-1] * inv[i] % mod
        self.mod = mod
        self.fac = fac
        self.inv = inv
        self.finv = finv

    def choose(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] * self.finv[k] % self.mod * self.finv[n-k] % self.mod

    def permuate(self, n, k=None):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        if k is None:
            return self.fac[n]
        return self.fac[n] * self.finv[n-k] % self.mod

    def multi_choose(self, n, k):
        return self.choose(n + k - 1, k)

################################

# for not use mod
class Dealer:
    def __init__(self, n):
        size = n + 1
        fac = [0] * size # factorial
        fac[:2] = 1, 1
        for i in range(2, size):
            fac[i] = fac[i-1] * i
        self.fac = fac

    def choose(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] // self.fac[k] // self.fac[n-k]

    def permuate(self, n, k=None):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        if k is None:
            return self.fac[n]
        return self.fac[n] // self.fac[n-k]

    def multi_choose(self, n, k):
        return self.choose(n + k - 1, k)

################################

from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

# use global MOD
def mul_mod(a, b):
    return a * b % MOD

def combinations_count_mod(n, r):
    r = min(r, n - r)
    numer = reduce(mul_mod, range(n, n - r, -1), 1)
    denom = reduce(mul_mod, range(1, r + 1), 1)
    denom = modinv(denom, MOD) #TODO import modinv
    return numer * denom

################################

# ref. https://qiita.com/derodero24/items/91b6468e66923a87f39f
# for tha case that n is big but r is small
def cmb(n, r):
    if n - r < r: r = n - r
    if n < r: return 0
    if n < 0 or r < 0: return 0
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser('This is hogehoge')
    args = parser.parse_args()

    mod = 998244353
    n = 65234

    magician = Magician(n, mod)
    assert math.factorial(n) % mod == magician.fac[n], 'hoge'

    for i in range(5 + 1):
        a = magician.choose(10, i)
        print(10, i, a) # debug

    for i in range(5 + 1):
        a = magician.permuate(10, i)
        print(10, i, a) # debug

    print('\33[32m' + 'end' + '\033[0m')

