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

import sys
sys.path

#from procan.graph import WeightedGraph
from procon.graph.main import WeightedGraph
from procon.bit_array.main import BitArray
from procon.two_d_arr.main import make_2d_arr


class HamiltonPath: # not cycle

    def __init__(self, graph):
        self.graph = graph
        BitArray.set_size(graph.size)
        self.dp = make_2d_arr(BitArray.size_as_set, BitArray.size, math.inf)
        for i in range(BitArray.size): # `i` is start vertex
            self.dp[BitArray.set(0, i, True)][i] = 0

    def solve(self):
        #print('self.graph') # debug
        #print(self.graph) # debug
        for s in range(BitArray.size_as_set): # this is ok
        #for s in BitArray.yield_lattice():
            if s == 0:
                continue
            #print("s", s, BitArray.repr(s)) # debug
            for frm in BitArray.iter_flg(s, True):
                for to, w in self.graph.edges[frm].items():
                    if BitArray.check(s, to) is True:
                        continue
                    new_ba_data = BitArray.get_set_data(s, to, True)
                    new_score = self.dp[s][frm] + w
                    if new_score < self.dp[new_ba_data][to]:
                        self.dp[new_ba_data][to] = new_score
        #print('self.dp') # debug
        #pp(self.dp) # debug
        return min(self.dp[-1])


#TODO save
if __name__ == '__main__':
    parser = argparse.ArgumentParser('This is hogehoge')
    args = parser.parse_args()

    graph = WeightedGraph(4)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 3, 3)

    ans = HamiltonPath(graph).solve()
    print('ans') # debug
    print(ans) # debug








    print('\33[32m' + 'end' + '\033[0m')
