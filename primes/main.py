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

# O(n log log n)
def enumerate_primes(upto):
    size = upto + 1
    is_prime = [True] * size
    is_prime[0] = False
    is_prime[1] = False
    for i in range(size):
        flg = is_prime[i]
        if flg is not True:
            continue
        key = i * 2
        while key < size:
            is_prime[key] = i
            key += i
    return is_prime

def to_prime_list(is_prime):
    primes = []
    for v, flg in enumerate(is_prime):
        if flg is True:
            primes.append(v)
    return primes

# ref. https://algo-logic.info/prime-fact/
# O(log n)
# primes: returned value of enumerate_primes
def prime_factorize(n, primes):
    #print("prime_factorize n", n) # debug
    factors = defaultdict(lambda: 0)
    while not n == 1:
        #print("n", n) # debug
        d = primes[n]
        if d is True:
            d = n
        n = n // d
        factors[d] += 1
    #print('factors') # debug
    #print(factors) # debug
    return factors

if __name__ == '__main__':
    #data = int(input())
    #data = list(map(int, input().split()))

    is_prime = enumerate_primes(100)
    primes = to_prime_list(is_prime)
    factors = prime_factorize(120, is_prime)
    print('factors') # debug
    pp(factors) # debug

    print('\33[32m' + 'end' + '\033[0m') # debug
