
from collections import deque
"""
l: data list
k: range width
return: max_idx[i] is max(a[key]) s.t. i - k + 1 <= key <= i
ref. https://qiita.com/kuuso1/items/318d42cd089a49eeb332
"""
def slide_max_index(l, k):
    n = len(l)
    max_idx = [-1] * n
    que = deque()
    for i in range(n):
        while len(que) > 0 and que[0] <= i - k:
            que.popleft()
        while len(que) > 0 and a[que[-1]] < a[i]:
        #while len(que) > 0 and a[que[-1]] > a[i]: # for min
            que.pop()
        que.append(i)
        max_idx[i] = que[0]
    return max_idx

