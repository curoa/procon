import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf

################################

TH_NAIVE = 10
#TH_DOUBLING = 40
TH_DOUBLING = 0

def rev_renge(m):
    i = m
    while i >= 0:
        yield i
        i -= 1

# sa: having sorted index
def sa_naive(s):
    def mine(i):
        return tuple(s[i:])
    n = len(s)
    sa = range(n)
    sa = sorted(sa, key=mine)
    return sa

S_TYPE = True
L_TYPE = False
def make_ls(s, n):
    ls = [False] * n # True: S-type, False: L-type
    for i in rev_renge(n - 2):
        now = s[i]
        nxt = s[i+1]
        if now == nxt:
            ls[i] = ls[i+1]
            continue
        ls[i] = (now < nxt)
    return ls

def make_sum_l_s(s, n, upper, ls):
    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if ls[i] == L_TYPE:
            sum_s[s[i]] += 1
        else:
            sum_l[s[i] + 1] += 1
    for i in range(upper + 1):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i+1] += sum_s[i]
    return sum_l, sum_s

# lms_map: lms_map[i] = j; s[i]から始まる LMS の LMS id は j
# lms: lms[j] = i; LMS id が j の LMS が始まる index i
def get_lms(ls, n):
    lms_map = [-1] * (n + 1)
    m = 0
    lms = []
    for i in range(1, n):
        if ls[i-1] == L_TYPE and ls[i] == S_TYPE:
            lms_map[i] = m
            m += 1
            lms.append(i)
    return lms_map, lms

# sorted_lms: ソートして若い順に LMS の index を持つ
def make_sorted_lms(sa, lms_map):
    sorted_lms = []
    for v in sa:
        if lms_map[v] != -1:
            sorted_lms.append(v)
    return sorted_lms

# return: 辞書順で i 番目の LMS sub string の開始 index start, 終了 index end を返す
# s[end] は LMS sub string に含まれない
def sa_is(s, upper):
    n = len(s)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        if s[0] < s[1]:
            return [0, 1]
        else:
            return [1, 0]
    if n < TH_NAIVE:
        return sa_naive(s)
    #if n < TH_DOUBLING:
    #    return sa_doubling(s)
    ls = make_ls(s, n)
    sum_l, sum_s = make_sum_l_s(s, n, upper, ls)
    lms_map, lms = get_lms(ls, n)

    # return sa: having sorted index
    def induce(lms):
        sa = [-1] * n
        # sum_s
        buf = sum_s[:] # char to count, that is head of bucket
        for i in lms:
            if i == n:
                continue
            sa[buf[s[i]]] = i
            buf[s[i]] += 1
        # sum_l
        buf = sum_l[:] # char to count, that is head of bucket
        sa[buf[s[n-1]]] = n - 1
        buf[s[n-1]] += 1
        for i in range(n):
            v = sa[i]
            prev = v - 1
            if v >= 1 and ls[prev] == L_TYPE:
                sa[buf[s[prev]]] = prev
                buf[s[prev]] += 1
        # sum_l 2
        buf = sum_l[:] # char to count, that is head of bucket
        for i in rev_renge(n - 1):
            v = sa[i]
            prev = v - 1
            if v >= 1 and ls[prev] == S_TYPE:
                buf[s[prev] + 1] -= 1
                sa[buf[s[prev] + 1]] = prev
        return sa

    sa = induce(lms)
    m = len(lms)
    if m:


        def make_recursive_s():
            sorted_lms = make_sorted_lms(sa, lms_map)

            def get_lms_sub_string(i):
                start = sorted_lms[i]
                end = lms[lms_map[start] + 1] if (lms_map[start] + 1 < m) else n
                return start, end

            def is_same_lms_sub_string(l, end_l, r, end_r):
                if end_l - l != end_r - r:
                    return False
                while l < end_l:
                    if s[l] != s[r]:
                        return False
                    l += 1
                    r += 1
                if l == n:
                    return False
                return True

            rec_s = [0] * m
            rec_upper = 0
            rec_s[lms_map[sorted_lms[0]]] = 0
            for i in range(1, m):
                l, end_l = get_lms_sub_string(i - 1)
                r, end_r = get_lms_sub_string(i)
                if not is_same_lms_sub_string(l, end_l, r, end_r):
                    rec_upper += 1
                rec_s[lms_map[sorted_lms[i]]] = rec_upper
            return rec_s, rec_upper

        rec_s, rec_upper = make_recursive_s()
        rec_sa = sa_is(rec_s, rec_upper)
        correct_lms = []
        for i in range(m):
            correct_lms.append(lms[rec_sa[i]])
        sa = induce(correct_lms)

    return sa

def to_int_list(s):
    new = []
    conv = {}
    i = 0
    for c in sorted(set(s)):
        if c not in conv:
            conv[c] = i
            i += 1
    for c in s:
        new.append(conv[c])
    #print("conv", conv) # debug
    return new, len(conv)

def make_lcp_array(s, sa):
    n = len(s)
    rank = [None] * n
    for i, r in enumerate(sa):
        rank[r] = i
    lcp = [None] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while j + h < n and i + h < n:
            if s[j+h] != s[i+h]:
                break
            # for next
            h += 1
        lcp[rank[i] - 1] = h
    print("lcp", lcp) # debug
    return lcp


def make_random_input():
    import random
    box = "abcde"
    n = 20
    s = []
    for _ in range(n):
        r = random.randrange(len(box))
        s.append(box[r])
    s = "".join(s)
    return s

def run(s):
    print("s", s) # debug
    s, upper = to_int_list(s)
    sa = sa_is(s, upper)
    lcp_arr = make_lcp_array(s, sa)
    return sa, lcp_arr

################################

def test(s=None):
    if s is None:
        s = make_random_input()
    sa, lcp_arr = run(s)
    sa2 = sa_naive(s) # debug
    myprint(s, sa, lcp_arr)
    if sa == sa2:
        #print("ok same") # debug
        pass
    else:
        print("err", sa2) # debug
        raise RuntimeError


def list_safe_get(l, index, default=None):
    if 0 <= index < len(l):
        return l[index]
    return default

def myprint(s_org, sa, lcp_arr):
    for r, i in enumerate(sa):
        print(list_safe_get(lcp_arr, r, "-"), s_org[i:])


if __name__ == '__main__':
    s = input().strip()
    for _ in range(30):
        test(s)
        pass

    print('\33[32m' + 'end' + '\033[0m') # debug

