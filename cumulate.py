#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc_cum(data):
    cum = [0] * (len(data) + 1)
    s = 0
    for i, v in enumerate(data, 1):
        s += v
        cum[i] = s
    return cum


################################

def make_cum_field(field):
    cum_field = make_2d_arr(n + 1, n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cum_field[i][j] = field[i-1][j-1] + cum_field[i-1][j] + cum_field[i][j-1] - cum_field[i-1][j-1]
    return cum_field

class CumField:

    def __init__(self, field):
        self.cum_field = make_cum_field(field)

    def calc(self, fi, fj, ti, tj):
        ti += 1
        tj += 1
        f = self.cum_field
        count = f[ti][tj] - f[fi][tj] - f[ti][fj] + f[fi][fj]
        return count

################################
