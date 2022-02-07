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


################################

class BitArray:

    size = None
    size_as_set = None

    @staticmethod
    def set_size(size):
        BitArray.size = size
        BitArray.size_as_set = 1 << size

    @staticmethod
    def repr(data):
        return "{}:{}".format(BitArray.size, bin(data)[2:].zfill(BitArray.size))

    @staticmethod
    def iter(data):
        for i in range(BitArray.size):
            yield BitArray.check(data, i)

    @staticmethod
    def iter_flg(data, flg):
        for i, b in enumerate(BitArray.iter(data)):
            if b == flg:
                yield i

    @staticmethod
    def loop():
        for i in range(BitArray.size_as_set):
            yield i

    @staticmethod
    def get_all_true():
        return (BitArray.size_as_set) - 1

    @staticmethod
    def get_all_false():
        return 0

    @staticmethod
    def is_all_1(data):
        return data == BitArray.get_all_true()

    @staticmethod
    def is_any_1(data):
        return data > 0

    @staticmethod
    def is_all_0(data):
        return data == 0

    @staticmethod
    def is_any_0(data):
        return data != BitArray.get_all_true()

    # ref. https://nixeneko.hatenablog.com/entry/2018/03/04/000000
    @staticmethod
    def count_1(data):
        return bin(data).count("1")

    @staticmethod
    def count_0(data):
        return size - BitArray.count_1()

    @staticmethod
    def get_flip(data):
        return BitArray.get_all_true() - data

    @staticmethod
    def check(data, i):
        return bool(data & (1 << i))

    @staticmethod
    def get_set_data(data, i, flg):
        if flg:
            return data | (1 << i)
        else:
            return data & get_flip(1 << i)

    @staticmethod
    def set(data, i, flg):
        data = BitArray.get_set_data(data, i, flg)
        return data

    #XXX NOT USE THIS. you should read 6 of https://jetbead.hatenablog.com/entry/20121202/1354406422
    #XXX yield is very slow
    #XXX storing in list is very very slow
    @staticmethod
    def yield_lattice():
        visited = set([0])
        visited_new = set()
        for i in range(BitArray.size):
            for v in visited:
                for u in range(BitArray.size):
                    if BitArray.check(v, u):
                        continue
                    new_v = BitArray.set(v, u, True)
                    """ # only lattice node
                    #if new_v in visited_new:
                    #    continue
                    #yield new_v
                    #"""
                    #""" # use last used
                    yield u, new_v, v
                    #"""
                    visited_new.add(new_v)
            visited, visited_new = visited_new, visited
            visited_new.clear()
            #print("visited", visited) # debug

    #XXX yield is very slow
    #XXX storing in list is very very slow
    @staticmethod
    def yield_subset(data):
        r = data
        while True:
            if r == 0:
                break
            print("r", r, bin(r)) # debug
            yield r
            r = (r - 1) & data


################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser('This is hogehoge')
    args = parser.parse_args()

    BitArray.size = 4
    ba = BitArray()
    ba.set(2, True)
    ba.set(2, False)
    ba.data = ba.get_all_true()
    print('ba') # debug
    print(ba) # debug
    print('ba.is_all_0()') # debug
    print(ba.is_all_0()) # debug
    print('ba.is_any_0()') # debug
    print(ba.is_any_0()) # debug

    print('bin(ba.get_all_true())') # debug
    print(bin(ba.get_all_true())) # debug

    print('\33[32m' + 'end' + '\033[0m')
