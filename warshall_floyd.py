"""
グラフの全点間距離を出す
"""
# ref. https://qiita.com/okaryo/items/8e6cd73f8a676b7a5d75
# O(n^3)
def warshall_floyd(n):
    for k in range(n): # via
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


