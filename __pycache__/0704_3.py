import heapq

# 隣接リスト形式のグラフ（有向・重み付き）
G = [
    [(1, 1)],
    [(2, 1)],
    [(3, 1)],
    []
]

def dijkstra(start, N):
    INF = float('inf')
    dist = [INF] * N  # 最短距離を格納するリスト
    dist[start] = 0   # 始点の距離は0

    # 優先度付きキュー（距離, 頂点）
    hq = [(0, start)]

    while hq:
        d, u = heapq.heappop(hq)
        if dist[u] < d:
            continue
        for v, cost in G[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(hq, (dist[v], v))

    return dist

# 実行してみる
N = 4
distances = dijkstra(0, N)

# 出力
for i, d in enumerate(distances):
    print(f"頂点{i}への最短距離：{d}")
