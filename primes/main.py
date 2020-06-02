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

def enumerate_primes(upto):
    size = upto + 1
    is_prime = [True] * size
    is_prime[0] = False
    is_prime[1] = False
    for i in range(size):
        flg = is_prime[i]
        if flg == False:
            continue
        key = i * 2
        while key < size:
            is_prime[key] = False
            key += i
    return is_prime

def to_prime_list(is_prime):
    primes = []
    for v, flg in enumerate(is_prime):
        print('v') # debug
        print(v) # debug
        if flg:
            primes.append(v)
    return primes

from collections import defaultdict
def prime_factorize(n, primes):
    factors = defaultdict(lambda: 0)
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
    return factors

if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))

    is_prime = enumerate_primes(100)
    primes = to_prime_list(is_prime)
    factors = prime_factorize(120, primes)
    print('factors') # debug
    pp(factors) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
