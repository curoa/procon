###############################################################################
# AVL木サンプルコード
###############################################################################

###############################################################################
# 共通定義
###############################################################################

class Node: # ノードの型
    def __init__(self, height, key, x):
        self.height = height # そのノードを根とする部分木の高さ
        self.key    = key    # そのノードのキー
        self.value  = x      # そのノードの値
        self.lst    = None   # 左部分木
        self.rst    = None   # 右部分木

# 部分木 t の高さを返す
def height(t): return 0 if t is None else t.height

# 左右の部分木の高さの差を返す。左が高いと正、右が高いと負
def bias(t): return height(t.lst) - height(t.rst)

# 左右の部分木の高さから、その木の高さを計算して修正する
def modHeight(t): t.height = 1 + max(height(t.lst), height(t.rst))

def rotateL(v): # ２分探索木 v の左回転。回転した木を返す
    u = v.rst; t2 = u.lst
    u.lst = v; v.rst = t2
    modHeight(u.lst)
    modHeight(u)
    return u
def rotateR(u): # ２分探索木 u の右回転。回転した木を返す
    v = u.lst; t2 = v.rst
    v.rst = u; u.lst = t2
    modHeight(v.rst)
    modHeight(v)
    return v
def rotateLR(t): # ２分探索木 t の二重回転(左回転 -> 右回転)。回転した木を返す
    t.lst = rotateL(t.lst)
    return rotateR(t)
def rotateRL(t): # ２分探索木 t の二重回転(右回転 -> 左回転)。回転した木を返す
    t.rst = rotateR(t.rst)
    return rotateL(t)

###############################################################################
# AVL木マップクラス
###############################################################################

class AVLMap:
    def __init__(self):
        self.root   = None  # AVL木の根。Node 型
        self.change = False # 修正が必要かを示すフラグ(True:必要, False:不要)
        self.lmax   = None  # 左部分木のキーの最大値
        self.value  = None  # lmax に対応する値

    ###########################################################################
    # バランス回復
    ###########################################################################

    # 挿入時の修正(balanceLi:左部分木への挿入, balanceRi:右部分木への挿入)
    def balanceLi(self, t): return self.balanceL(t)
    def balanceRi(self, t): return self.balanceR(t)

    # 削除時の修正(balanceLd:左部分木での削除, balanceRd:右部分木での削除)
    def balanceLd(self, t): return self.balanceR(t)
    def balanceRd(self, t): return self.balanceL(t)

    # 部分木 t のバランスを回復して戻り値で返す
    # 左部分木への挿入に伴うAVL木の修正
    # 右部分木での削除に伴うAVL木の修正
    def balanceL(self, t):
        if not self.change: return t
        h = height(t)
        if bias(t) == 2:
            if bias(t.lst) >= 0:
                t = rotateR(t)
            else:
                t = rotateLR(t)
        else: modHeight(t)
        self.change = (h != height(t))
        return t

    # 部分木 t のバランスを回復して戻り値で返す
    # 右部分木への挿入に伴うAVL木の修正
    # 左部分木での削除に伴うAVL木の修正
    def balanceR(self, t):
        if not self.change: return t
        h = height(t)
        if bias(t) == -2:
            if bias(t.rst) <= 0:
                t = rotateL(t)
            else:
                t = rotateRL(t)
        else: modHeight(t)
        self.change = (h != height(t))
        return t

    ###########################################################################
    # insert(挿入)
    ###########################################################################

    # エントリー(key, x のペア)を挿入する
    def insert(self, key, x): self.root = self.insert_sub(self.root, key, x)

    def insert_sub(self, t, key, x):
        if t is None:
            self.change = True
            return Node(1, key, x)
        elif key < t.key:
            t.lst = self.insert_sub(t.lst, key, x)
            return self.balanceLi(t)
        elif key > t.key:
            t.rst = self.insert_sub(t.rst, key, x)
            return self.balanceRi(t)
        else:
            self.change = False
            t.value = x
            return t

    ###########################################################################
    # delete(削除)
    ###########################################################################

    # key で指すエントリー(ノード)を削除する
    def delete(self, key): self.root = self.delete_sub(self.root, key)

    def delete_sub(self, t, key):
        if t is None:
            self.change = False
            return None
        elif key < t.key:
            t.lst = self.delete_sub(t.lst, key)
            return self.balanceLd(t)
        elif key > t.key:
            t.rst = self.delete_sub(t.rst, key)
            return self.balanceRd(t)
        else:
            if t.lst is None:
                self.change = True
                return t.rst # 右部分木を昇格させる
            else:
                t.lst = self.delete_max(t.lst) # 左部分木の最大値を削除する
                t.key = self.lmax # 左部分木の削除した最大値で置き換える
                t.value = self.value
                return self.balanceLd(t)

    # 部分木 t の最大値のノードを削除する
    # 戻り値は削除により修正された部分木
    # 削除した最大値を lmax に保存する
    def delete_max(self, t):
        if t.rst is not None:
            t.rst = self.delete_max(t.rst)
            return self.balanceRd(t)
        else:
            self.change = True
            self.lmax = t.key # 部分木のキーの最大値を保存
            self.value = t.value
            return t.lst # 左部分木を昇格させる

    ###########################################################################
    # member(検索)等
    ###########################################################################

    # キーの検索。ヒットすれば True、しなければ False
    def member(self, key):
        t = self.root
        while t is not None:
            if key < t.key:
                t = t.lst
            elif key > t.key:
                t = t.rst
            else:
                return True
        return False

    # キーから値を得る。キーがヒットしない場合は None を返す
    def lookup(self, key):
        t = self.root
        while t is not None:
            if key < t.key:
                t = t.lst
            elif key > t.key:
                t = t.rst
            else:
                return t.value
        return None

    # マップが空なら True、空でないなら False
    def isEmpty(self): return self.root is None

    # マップを空にする
    def clear(self): self.root = None

    # キーのリスト
    def keys(self): return keys_sub(self.root)

    # 値のリスト
    def values(self): return values_sub(self.root)

    # エントリーのリスト
    def items(self): return items_sub(self.root)

    # マップのサイズ
    def size(self): return len(self.keys())

    def __contains__(self, key): self.member(key)
    def __getitem__(self, key): return self.lookup(key)
    def __setitem__(self, key, x): return self.insert(key, x)
    def __delitem__(self, key): self.delete(key)
    def __bool__(self): return not self.isEmpty()
    def __len__(self): return self.size()
    def __iter__(self): return iter(self.keys())

    ###########################################################################
    # Debug 用メソッド
    ###########################################################################

    # AVL木をグラフ文字列に変換する
    def __str__(self): return toGraph("", "", self.root).rstrip()

    # AVL木のバランスが取れているか確認する
    def balanced(self): return balanced(self.root)

    # ２分探索木になっているか確認する
    def bstValid(self): return bstValid(self.root)

###############################################################################
# 作業メソッド
###############################################################################

def keys_sub(t):
    if t is None: return []
    return keys_sub(t.lst) + [t.key] + keys_sub(t.rst)

def values_sub(t):
    if t is None: return []
    return values_sub(t.lst) + [t.value] + values_sub(t.rst)

def items_sub(t):
    if t is None: return []
    return items_sub(t.lst) + [(t.key, t.value)] + items_sub(t.rst)

###############################################################################
# Debug 用作業メソッド
###############################################################################

def toGraph(head, bar, t):
    graph = ""
    if t != None:
        graph += toGraph(head + "    ", "／", t.rst)
        node = str(t.height)
        node += ":" + str(t.key) + ":" + str(t.value)
        graph += head + bar + node + "\n"
        graph += toGraph(head + "    ", "＼", t.lst)
    return graph

def balanced(t):
    if t is None: return True
    return abs(bias(t)) <= 1 and balanced(t.lst) and balanced(t.rst)

def bstValid(t):
    if t is None: return True
    flag = small(t.key, t.lst) and large(t.key, t.rst)
    return flag and bstValid(t.lst) and bstValid(t.rst)
def small(key, t):
    if t is None: return True
    return t.key < key and small(key, t.lst) and small(key, t.rst)
def large(key, t):
    if t is None: return True
    return t.key > key and large(key, t.lst) and large(key, t.rst)

###############################################################################
# モジュールテストルーチン
###############################################################################

if __name__ == '__main__':
    import random
    n = 30
    m = AVLMap() # AVL木マップを生成
    keys = list(range(n))
    random.shuffle(keys)
    for i, key in enumerate(keys): m[key] = i
    print(m)
    print()
    for key in sorted(keys[:5]):
        print("m[{0:>2}] == {1}".format(key, m[key]))
    print()
    print("size: ", len(m))
    print("keys: ", m.keys())

    N = 100000
    m.clear()
    answer = {}
    insertErrors = 0
    for i in range(N):
        key = random.randrange(N)
        m.insert(key, i)
        answer[key] = i
    for key in answer:
        if m[key] != answer[key]:
            insertErrors += 1
    deleteKeys = random.sample(answer.keys(), len(answer)//2)
    deleteErrors = 0
    for key in deleteKeys: m.delete(key)
    for key in deleteKeys:
        if key in m:
            deleteErrors += 1

    def okng(flag): return "OK" if flag else "NG"
    print()
    print("バランス:  ", okng(m.balanced()))
    print("２分探索木:", okng(m.bstValid()))
    print("挿入:      ", okng(insertErrors == 0))
    print("削除:      ", okng(deleteErrors == 0))
    for key in m: del m[key]
    print("全削除:    ", okng(not m))

###############################################################################
