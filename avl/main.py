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

#XXX use python, not pypy. because recursive func used

# ref. http://wwwa.pikara.ne.jp/okojisan/avl-tree/python.html

class Node:
    def __init__(self, height, key, value):
        self.height = height
        self.key = key
        self.value = value
        self.small = None
        self.large = None

    def __iter__(self):
        if self.small is not None:
            for n in self.small:
                yield n
        yield self
        if self.large is not None:
            for n in self.large:
                yield n

def height(tree):
    if tree is None:
        return 0
    return tree.height

def bias(tree):
    return height(tree.small) - height(tree.large)

def calc_height(tree):
    tree.height = 1 + max(height(tree.small), height(tree.large))

def rotate_to_small(p):
    c = p.large
    n = c.small
    p.large = n
    c.small = p
    calc_height(p)
    calc_height(c)
    return c

def rotate_to_large(p):
    c = p.small
    n = c.large
    p.small = n
    c.large = p
    calc_height(p)
    calc_height(c)
    return c

def rotate_to_small_large(tree):
    tree.small = rotate_to_small(tree.small)
    return rotate_to_large(tree)

def rotate_to_large_small(tree):
    tree.large = rotate_to_large(tree.large)
    return rotate_to_small(tree)

class AVL:

    def __init__(self):
        self.root = None
        self.changed = False
        self.small_max_key = None
        self.small_max_value = None

    def __repr__(self):
        return to_graph("*", "-", self.root)

    def balance_for_insert_small(self, tree):
        return self.balance_small(tree)

    def balance_for_insert_large(self, tree):
        return self.balance_large(tree)

    def balance_for_delete_small(self, tree):
        return self.balance_large(tree)

    def balance_for_delete_large(self, tree):
        return self.balance_small(tree)

    def balance_small(self, tree):
        if not self.changed:
            return tree
        h = height(tree)
        if bias(tree) == 2:
            if bias(tree.small) >= 0:
                tree = rotate_to_large(tree)
            else:
                tree = rotate_to_small_large(tree)
        else:
            calc_height(tree)
        self.changed = (h != height(tree))
        return tree

    def balance_large(self, tree):
        if not self.changed:
            return tree
        h = height(tree)
        if bias(tree) == -2:
            if bias(tree.large) <= 0:
                tree = rotate_to_small(tree)
            else:
                tree = rotate_to_large_small(tree)
        else:
            calc_height(tree)
        self.changed = (h != height(tree))
        return tree

    """
    insert
    """

    def insert(self, key, value):
        self.root = self.insert_sub(self.root, key, value)

    def insert_sub(self, tree, key, value):
        if tree is None:
            self.changed = True
            return Node(1, key, value)
        elif key < tree.key:
            tree.small = self.insert_sub(tree.small, key, value)
            return self.balance_for_insert_small(tree)
        elif key > tree.key:
            tree.large = self.insert_sub(tree.large, key, value)
            return self.balance_for_insert_large(tree)
        else:
            self.changed = False
            tree.value = value
            return tree

    """
    delete
    """

    def delete(self, key):
        self.root = self.delete_sub(self.root, key)

    def delete_sub(self, tree, key):
        if tree is None:
            self.changed = False
            return None
        elif key < tree.key:
            tree.small = self.delete_sub(tree.small, key)
            return self.balance_for_delete_small(tree)
        elif key > tree.key:
            tree.large = self.delete_sub(tree.large, key)
            return self.balance_for_delete_large(tree)
        else:
            if tree.small is None:
                self.changed = True
                return tree.large
            else:
                tree.small = self.delete_max(tree.small)
                tree.key = self.small_max_key
                tree.value = self.small_max_value
                return self.balance_for_delete_small(tree)

    def delete_max(self, tree):
        if tree.large is not None:
            tree.large = self.delete_max(tree.large)
            return self.balance_for_delete_large(tree)
        else:
            self.changed = True
            self.small_max_key = tree.key
            self.small_max_value = tree.value
            return tree.small

    """
    operation
    """

    def member(self, key):
        tree = self.root
        while not (tree is None):
            if key < tree.key:
                tree = tree.small
            elif key > tree.key:
                tree = tree.large
            else:
                return True
        return False

    def get(self, key):
        tree = self.root
        while not (tree is None):
            if key < tree.key:
                tree = tree.small
            elif key > tree.key:
                tree = tree.large
            else:
                return tree.value
        return None

    # return minimal hit, which key >= key
    # ref. https://cpprefjp.github.io/reference/map/map/lower_bound.html
    def lower_bound(self, key):
        tree = self.root
        minimal = math.inf
        while not (tree is None):
            if key < tree.key:
                minimal = min(minimal, tree.value)
                tree = tree.small
            elif key > tree.key:
                tree = tree.large
            else:
                return tree.value
        return minimal

    # return minimal hit, which key > key
    # ref. https://cpprefjp.github.io/reference/map/map/upper_bound.html
    def upper_bound(self, key):
        tree = self.root
        minimal = math.inf
        while not (tree is None):
            if key < tree.key:
                minimal = min(minimal, tree.value)
                tree = tree.small
            elif key > tree.key:
                tree = tree.large
            else:
                # same as key > tree.large
                tree = tree.large
        return minimal

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def keys(self):
        return keys_sub(self.root)

    def __iter__(self): return self.root.__iter__()
    def __contains__(self, key): self.member(key)
    def __getitem__(self, key): return self.get(key)
    def __setitem__(self, key, value): return self.insert(key, value)

    """
    debug
    """

    def __str__(self):
        return toGraph("", "", self.root).rstrip()

    def balanced(self):
        return balanced(self.root)

    def valid_binary_search_tree(self):
        return valid_binary_search_tree(self.root)


def keys_sub(tree):
    if tree is None:
        return []
    return keys_sub(tree.small) + [tree.key] + keys_sub(tree.large)

def to_graph(head, bar, tree):
    graph = ""
    if tree is not None:
        graph += to_graph(head + "  ", "/", tree.small)
        node = "{}:{}:{}".format(tree.height, tree.key, tree.value)
        graph += head + bar + node + "\n"
        graph += to_graph(head + "  ", "\\", tree.large)
    return graph

def balanced(tree):
    if tree is None:
        return True
    return abs(bias(tree)) <= 1 and balanced(tree.small) and balanced(tree.large)

def valid_binary_search_tree(tree):
    if tree is None:
        return True
    flg = check_small(tree.key, tree.small) and check_large(tree.key, tree.large)
    return flg and valid_binary_search_tree(tree.small) and valid_binary_search_tree(tree.large)

def check_small(key, tree):
    if tree is None:
        return True
    return tree.key < key and check_small(key, tree.small) and check_small(key, tree.large)

def check_large(key, tree):
    if tree is None:
        return True
    return tree.key > key and check_large(key, tree.small) and check_large(key, tree.large)

################################



if __name__ == '__main__':
    import random
    def okng(flg): return "OK" if flg else "NG!"

    n = 30
    tree = AVL()
    keys = list(range(n))
    random.shuffle(keys)
    for i, key in enumerate(keys):
        tree[key] = i
    print(tree)
    print()
    for key in sorted(keys[:5]):
        print("tree[{0:>2}] == {1}".format(key, tree[key]))
    print()


    n = 100000
    tree.clear()
    answer = {}
    insert_errors = 0
    for i in range(n):
        key = random.randrange(n)
        tree.insert(key, i)
        answer[key] = i
    for key in answer:
        if tree[key] != answer[key]:
            insert_errors += 1
    delete_keys = random.sample(answer.keys(), len(answer) // 2)
    delete_errors = 0
    for key in delete_keys:
        tree.delete(key)
    for key in delete_keys:
        if key in tree:
            delete_errors += 1

    print()
    print("balance  ", okng(tree.balanced()))
    print("valid    ", okng(tree.valid_binary_search_tree()))
    print("insert   ", okng(insert_errors == 0))
    print("delete   ", okng(delete_errors == 0))
    for key in tree.keys():
        tree.delete(key)
    print("all      ", okng(tree.root is None))




    print('\33[32m' + 'end' + '\033[0m')
