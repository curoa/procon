#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cumulate(data):
    cum = [0]
    s = 0
    for v in data:
        s += v
        cum.append(s)
    return cum

