import math

# ref. https://betrue12.hateblo.jp/entry/2020/09/23/005940
# ref. https://betrue12.hateblo.jp/entry/2020/09/22/194541
# ref. https://atcoder.github.io/ac-library/document_ja/lazysegtree.html
# ref. https://atcoder.jp/contests/abc223/submissions/26659684
class LazySegmentTree:
    #seg = LazySegmentTree(op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, N, array=None):
    def __init__(self, op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, N, array=None):
        #  それぞれ  Xの演算, 単位元, f(x), f\circ g,             Xの恒等変換
        # M が X に作用する
        #__slots__ = ["op_X",  "e_X",  "mapping","compose","id_M","N","log","N0","data","lazy"]
        self.e_X = e_X; self.op_X = op_X; self.mapping = mapping; self.compose = composision_of_Aut_X; self.id_M = id_M = id_of_Aut_X
        self.N = N
        self.log = (N-1).bit_length()
        self.N0 = 1<<self.log
        self.data = [e_X]*(2*self.N0)
        self.lazy = [id_M]*self.N0
        if array is not None:
            assert N == len(array)
            self.data[self.N0:self.N0+self.N] = array
            for i in range(self.N0-1,0,-1): self.update(i)

    # 1点更新
    def point_set(self, p, x):
        p += self.N0
        for i in range(self.log, 0,-1):
            self.push(p>>i)
        self.data[p] = x
        for i in range(1, self.log + 1):
            self.update(p>>i)

    # 1点取得
    def point_get(self, p):
        p += self.N0
        for i in range(self.log, 0, -1):
            self.push(p>>i)
        return self.data[p]

    # 半開区間[L,R)をopでまとめる, query
    def prod(self, l, r):
        if l == r: return self.e_X
        l += self.N0
        r += self.N0
        for i in range(self.log, 0, -1):
            if (l>>i)<<i != l:
                self.push(l>>i)
            if (r>>i)<<i != r:
                self.push(r>>i)

        sml = smr = self.e_X
        while l < r:
            if l & 1:
                sml = self.op_X(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op_X(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op_X(sml, smr)

    # 全体をopでまとめる
    def all_prod(self): return self.data[1]

    # 1点作用
    def apply_point(self, p, f):
        p += self.N0
        for i in range(self.log, 0, -1):
            self.push(p>>i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log + 1):
            self.update(p>>i)

    # 区間作用, update
    def apply(self, l, r, f):
        if l == r: return
        l += self.N0
        r += self.N0
        for i in range(self.log, 0, -1):
            if (l>>i)<<i != l:
                self.push(l>>i)
            if (r>>i)<<i != r:
                self.push((r-1)>>i)

        l2, r2 = l, r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1

        l, r = l2, r2
        for i in range(1, self.log + 1):
            if (l>>i)<<i != l:
                self.update(l>>i)
            if (r>>i)<<i != r:
                self.update((r-1)>>i)

    """
    始点 l を固定
    f(x_l*...*x_{r-1}) が True になる最大の r
    つまり TTTTFFFF となるとき、F となる最小の添え字
    存在しない場合 n が返る
    f(e_M) = True でないと壊れる
    """
    def max_right(self, l, g):
        if l == self.N: return self.N
        l += self.N0
        for i in range(self.log, 0, -1): self.push(l>>i)
        sm = self.e_X
        while True:
            while l&1 == 0:
                l >>= 1
            if not g(self.op_X(sm, self.data[l])):
                while l < self.N0:
                    self.push(l)
                    l *= 2
                    if g(self.op_X(sm, self.data[l])):
                        sm = self.op_X(sm, self.data[l])
                        l += 1
                return l - self.N0
            sm = self.op_X(sm, self.data[l])
            l += 1
            if l&-l == l: break
        return self.N

    """
    終点 r を固定
    f(x_l*...*x_{r-1}) が True になる最小の l
    つまり FFFFTTTT となるとき、T となる最小の添え字
    存在しない場合 r が返る
    f(e_M) = True でないと壊れる
    """
    def min_left(self, r, g):
        if r == 0: return 0
        r += self.N0
        for i in range(self.log, 0, -1): self.push((r-1)>>i)
        sm = self.e_X
        while True:
            r -= 1
            while r>1 and r&1:
                r >>= 1
            if not g(self.op_X(self.data[r], sm)):
                while r < self.N0:
                    self.push(r)
                    r = 2*r + 1
                    if g(self.op_X(self.data[r], sm)):
                        sm = self.op_X(self.data[r], sm)
                        r -= 1
                return r + 1 - self.N0
            sm = self.op_X(self.data[r], sm)
            if r&-r == r: break
        return 0

    # 以下内部関数
    def update(self, k):
        self.data[k] = self.op_X(self.data[2*k], self.data[2*k+1])

    def all_apply(self, k, f):
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.N0:
            self.lazy[k] = self.compose(f, self.lazy[k])

    def push(self, k): #propagate と同じ
        if self.lazy[k] is self.id_M: return
        self.data[2*k  ] = self.mapping(self.lazy[k], self.data[2*k])
        self.data[2*k+1] = self.mapping(self.lazy[k], self.data[2*k+1])
        if 2*k < self.N0:
            self.lazy[2*k]   = self.compose(self.lazy[k], self.lazy[2*k])
            self.lazy[2*k+1] = self.compose(self.lazy[k], self.lazy[2*k+1])
        self.lazy[k] = self.id_M

def init_st_add_min(size, array):
    import operator
    op_X = min
    e_X = math.inf
    mapping = operator.add
    composision_of_Aut_X = operator.add
    id_of_Aut_X = 0
    return LazySegmentTree(op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, size, array)

def init_st_add_max(size, array):
    import operator
    op_X = max
    e_X = -1 * math.inf
    mapping = operator.add
    composision_of_Aut_X = operator.add
    id_of_Aut_X = 0
    return LazySegmentTree(op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, size, array)

def init_st_add_sum(size):
    import operator
    # s: (value, size)
    op_X = lambda s1, s2: (s1[0] + s2[0], s1[1] + s2[1])
    e_X = (0, 0)
    mapping = lambda f, s: (s[0] + f * s[1], s[1])
    composision_of_Aut_X = operator.add
    id_of_Aut_X = 0
    array = [(0, 1)] * size
    return LazySegmentTree(op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, size, array)

def init_st_update_min(size, array):
    import operator
    op_X = min
    e_X = math.inf
    mapping = lambda f, s: s if math.isinf(f) else f
    composision_of_Aut_X = lambda f1, f2: f2 if math.isinf(f1) else f1
    id_of_Aut_X = math.inf
    return LazySegmentTree(op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, size, array)

def init_st_update_max(size, array):
    import operator
    op_X = max
    e_X = -1 * math.inf
    mapping = lambda f, s: s if math.isinf(f) else f
    composision_of_Aut_X = lambda f1, f2: f2 if math.isinf(f1) else f1
    id_of_Aut_X = math.inf
    return LazySegmentTree(op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, size, array)

def init_st_update_sum(size):
    def f_mapping(f, s):
        if not math.inf(f):
            s[0] = f * s[1]
        return s
    import operator
    # s: (value, size)
    op_X = lambda s1, s2: (s1[0] + s2[0], s1[1] + s2[1])
    e_X = (0, 0)
    mapping = f_mapping
    composision_of_Aut_X = lambda f1, f2: f2 if math.isinf(f1) else f1
    id_of_Aut_X = math.inf
    array = [(0, 1)] * size
    return LazySegmentTree(op_X, e_X, mapping, composision_of_Aut_X, id_of_Aut_X, size, array)

if __name__ == '__main__':
    size = 10
    st = init_st_add_sum(size)
    st.apply(4, 7, 1)
    print("st.prod(0, 4)", st.prod(0, 4)) # debug
    print("st.prod(0, 5)", st.prod(0, 5)) # debug
    print("st.prod(6, 8)", st.prod(6, 8)) # debug
    print("st.prod(5, 6)", st.prod(5, 6)) # debug
    print("st.prod(4, 7)", st.prod(4, 7)) # debug



