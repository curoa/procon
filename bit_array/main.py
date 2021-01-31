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

    size = -1
    set_size = -1

    @staticmethod
    def set_size(size):
        if BitArray.size != -1:
            raise RuntimeError("Already BitArray.size is set")
        BitArray.size = size
        BitArray.set_size = 1 << size

    def __init__(self, data=0):
        if self.size == -1:
            raise RuntimeError("please set BitArray.size")
        self.data = data

    def __repr__(self):
        self.size
        return "{}:{}".format(self.size, bin(self.data)[2:].zfill(self.size))

    def __iter__(self):
        for i in range(self.size):
            yield self.check(i)

    def my_iter(self, flg):
        for i, b in enumerate(self):
            if b == flg:
                yield i

    @staticmethod
    def loop():
        for i in range(BitArray.set_size):
            yield BitArray(i)

    @staticmethod
    def get_all_true():
        return (BitArray.set_size) - 1

    @staticmethod
    def get_all_false():
        return 0

    def is_all_1(self):
        return self.data == self.get_all_true()

    def is_any_1(self):
        return self.data > 0

    def is_all_0(self):
        return self.data == 0

    def is_any_0(self):
        return self.data != self.get_all_true()

    # ref. https://nixeneko.hatenablog.com/entry/2018/03/04/000000
    def count_1(self):
        return bin(self.data).count("1")

    def count_0(self):
        return self.size - self.count_1()

    def get_flip(self, data=None):
        if data is None:
            data = self.data
        return self.get_all_true() - data

    def check(self, i):
        return bool(self.data & (1 << i))

    # not modify self
    def get_set_data(self, i, flg):
        if flg:
            return self.data | (1 << i)
        else:
            return self.data & self.get_flip(1 << i)

    def set(self, i, flg):
        self.data = self.get_set_data(i, flg)
        return self


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
