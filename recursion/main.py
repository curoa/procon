#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
import pysnooper # debug

def ternary_op(flg, a, b):
    if flg:
        return a
    else:
        return b

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
# Queue is very slow
from collections import defaultdict

#XXX Honestly, I don't recommend this. try python and speed tuning
#XXX if you do any task after stack.add(), maybe it breaks code
# global stack
# please stack.append() in recursive function. not call recursion()
def recursion(f):
    while not len(stack) == 0:
        args = stack.pop()
        f(args)
        #f(*args)


# used by recursion
def calc(v):
    if v > 10:
        return
    v += 1
    print("v", v) # debug
    #calc(v)
    stack.append(v)

def fib_org(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    return fib_org(i - 1) + fib_org(i - 2)

def fib(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    mystack = [i]
    result = []
    while len(mystack) > 0:
        v = mystack.pop()
        if v <= 1:
            result.append(1)
            continue
        mystack.append(v - 1)
        mystack.append(v - 2)
        """
        while len(result) >= 2:
            a = result.pop()
            b = result.pop()
            result.append(a + b)
        """
    while len(result) >= 2:
        a = result.pop()
        b = result.pop()
        result.append(a + b)
    print("mystack", mystack) # debug
    print("result", result) # debug

if __name__ == '__main__':
    #calc(1)
    stack = [1]
    recursion(calc)

    print("fib_org(9)", fib_org(9)) # debug

    fib(9)

    """
    i = 9
    stack = []
    result = []
    stack.append(i)
    recursion(fib)
    r = result.pop()
    print("i, r", i, r) # debug
    """

    print('\33[32m' + 'end' + '\033[0m') # debug

