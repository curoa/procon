import time
import unittest


# ref. https://matsu7874.hatenablog.com/entry/2018/07/30/000705
def enumerate_n_omino(n: int):
    """
    Redelmeier's algorithm
    fixed（回転・反転を考慮しない）なポリオミノを列挙する。
    """
    if n < 1:
        return []

    UNORDER = -1
    MAX_Y = n
    MAX_X = 2 * n - 1
    X_CENTER = n - 1
    DYDX = ((1, 0), (0, 1), (-1, 0), (0, -1))

    ominos = []

    visited = [[False] * MAX_X for i in range(MAX_Y)]
    visited_queue = []
    order = [[UNORDER] * MAX_X for i in range(MAX_Y)]
    ordered_queue = []
    border = set()

    # (0,0)から探索を始める
    visited_queue.append((0, X_CENTER))
    visited[0][X_CENTER] = True
    order[0][X_CENTER] = 0

    max_visited = 0
    next_order = 1
    max_x = X_CENTER
    min_x = X_CENTER
    max_y = 0

    def dfs(y: int, x: int, last: int) -> None:
        nonlocal next_order, max_visited, ominos, max_x, min_x, max_y

        if last == 0:
            ominos.append(
                [row[min_x:max_x + 1] for row in visited[:max_y + 1]])
            return

        # (y, x)に隣接セルに付番する
        for dy, dx in DYDX:
            ny = y + dy
            nx = x + dx
            if (ny == 0 and nx < n) or not (0 <= ny < MAX_Y and 0 <= nx < MAX_X):
                continue
            if order[ny][nx] == UNORDER:
                order[ny][nx] = next_order
                next_order += 1
                border.add((ny, nx))
                ordered_queue.append((y, x, ny, nx))

        # セルを追加可能な箇所を列挙する
        for ny, nx in list(border):
            # if (ny == 0 and nx < n) or not (0 <= ny < MAX_Y and 0 <= nx < MAX_X):
            #     continue
            if order[ny][nx] > max_visited:
                # 深さ+1
                visited[ny][nx] = True
                visited_queue.append((ny, nx))
                pre_max_visited = max_visited
                max_visited = order[ny][nx]
                border.remove((ny, nx))

                pre_max_y = max_y
                pre_max_x = max_x
                pre_min_x = min_x
                max_y = max(max_y, ny)
                max_x = max(max_x, nx)
                min_x = min(min_x, nx)

                # 再帰
                dfs(ny, nx, last - 1)

                # 深さ-1
                # 遷移先で付番したものをキャンセルする
                while ordered_queue and (ny, nx) == (ordered_queue[-1][0], ordered_queue[-1][1]):
                    _y, _x, py, px = ordered_queue.pop()
                    order[py][px] = UNORDER
                max_y = pre_max_y
                max_x = pre_max_x
                min_x = pre_min_x
                border.add((ny, nx))
                max_visited = pre_max_visited
                visited_queue.pop()
                visited[ny][nx] = False

    dfs(0, X_CENTER, X_CENTER)

    return ominos


class TestEnumerateNOmino(unittest.TestCase):
    def test_enumerate_n_polyomino(self):
        cases = ((1, 1), (2, 2), (3, 6), (4, 19), (5, 63), (6, 216),
                 (7, 760), (8, 2725), (9, 9910), (10, 36446))
        for i, expect in cases:
            with self.subTest(i=i, expect=expect):
                ominos = enumerate_n_omino(i)
                self.assertEqual(len(ominos), expect)


def main():
    ominos = enumerate_n_omino(3)
    for omino in ominos:
        for row in omino:
            for c in row:
                if c:
                    print("#", end="")
                else:
                    print("-", end="")
            print("")
            #print(''.join(['#' if c else '-' for c in row]))
        print()
    print()
    """
    print('|n|n-omino|elapsed[s]|')
    print('|---:|---:|---:|')
    for i in range(1, 15):
        start = time.time()
        ominos = enumerate_n_omino(i)
        elapsed = time.time() - start
        print('|{}|{}|{:04f}|'.format(i, len(ominos), elapsed))
    """


if __name__ == '__main__':
    main()
