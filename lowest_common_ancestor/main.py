from pprint import pprint as pp
from pprint import pformat as pf

from procon.graph.main import Graph
from procon.two_d_arr.main import make_2d_arr

################################

def prepare(graph):
    # global stack
    # please stack.append() in recursive function. not call recursion()
    def _recursion(f):
        while not len(stack) == 0:
            args = stack.pop()
            f(*args)
    def _dfs(v, p):
        #print("v, p", v, p) # debug
        parent[0][v] = p
        depth[v] = depth[p] + 1
        for to in graph.edges[v]:
            if to == p:
                continue
            stack.append((to, v))
            #_dfs(to, v)
    bit_size = graph.size.bit_length()
    parent = make_2d_arr(bit_size, graph.size, 0) # parent[k][v]: `2^k` steps parent of `v`
    depth = [-1] * graph.size
    stack = []
    stack.append((0, 0))
    _recursion(_dfs)
    #_dfs(0, 0) # treat over parent as 0
    for i in range(1, bit_size):
        for j in range(graph.size):
            parent[i][j] = parent[i-1][parent[i-1][j]]
    return parent, depth


def lca(v1, v2, parent, depth):
    if depth[v1] < depth[v2]:
        v1, v2 = v2, v1
    for i in range(len(parent) - 1, 0 - 1, -1):
        if depth[v1] - depth[v2] >= (1 << i):
            v1 = parent[i][v1]
    if v1 == v2:
        return v1
    for i in range(len(parent) - 1, 0 - 1, -1):
        if parent[i][v1] != parent[i][v2]:
            v1 = parent[i][v1]
            v2 = parent[i][v2]
    return parent[0][v1]

################################


if __name__ == '__main__':
    n = int(input())
    graph = Graph(n)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        a -= 1; b -= 1
        graph.add_edge(a, b)
    parent, depth = prepare(graph)
    print('parent') # debug
    pp(parent) # debug
    print("depth", depth) # debug
    for i in range(n):
        for j in range(i, n):
            a = lca(i, j, parent, depth)
            print("i, j, a", i, j, a) # debug
