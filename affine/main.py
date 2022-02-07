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




################################

# ref. https://imagingsolution.net/imaging/affine-transformation/

def make_2d_arr(s1, s2, default=0):
    a = [None] * s1
    for i, _ in enumerate(a):
        a[i] = [default] * s2
    return a

def get_base_matrix():
    z = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            ]
    return z

def matrix_inner_product(x, y):
    z = make_2d_arr(len(x), len(y[0]))
    for i, _z in enumerate(z):
        for j in range(len(_z)):
            v = 0
            for k in range(len(x[i])):
                v += x[i][k] * y[k][j]
            z[i][j] = v
    return z

# mat: 2x2 matrix 
def move_point(mat, xy):
    new_x = mat[0][0] * xy[0] + mat[0][1] * xy[1]
    new_y = mat[1][0] * xy[0] + mat[1][1] * xy[1]
    return new_x, new_y


# angle: 0-360
# counter clockwise
def get_rotate_matrix(angle):
    x = make_2d_arr(3, 3)
    x[0][0] = math.cos(math.radians(angle))
    x[0][1] = -1 * math.sin(math.radians(angle))
    x[1][0] = math.sin(math.radians(angle))
    x[1][1] = math.cos(math.radians(angle))
    x[2][2] = 1
    return x

op_clock_rev = [[0, -1], [1, 0]] # angle 90
op_clock = [[0, 1], [-1, 0]] # angle -90

def get_slide_matrix(x, y):
    z = get_base_matrix()
    z[0][2] = x
    z[1][2] = y
    return z

def get_x_flip_matrix():
    z = get_base_matrix()
    z[0][0] = -1
    return z

def get_y_flip_matrix():
    z = get_base_matrix()
    z[1][1] = -1
    return z

################################

if __name__ == '__main__':
    z = get_rotate_matrix(90)
    print('z') # debug
    print(z) # debug


    print('\33[32m' + 'end' + '\033[0m') # debug
