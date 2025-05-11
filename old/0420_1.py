def main():
    n, m = map(int, input().split())
    a = []
    idx = [[] for _ in range(n)]
    cnt = [0] * m

    for i in range(m):
        k, *rest = map(int, input().split())
        # k個の値が改行でくる場合
        if len(rest) < k:
            rest += list(map(int, input().split()))
        cnt[i] = k
        a.append([x - 1 for x in rest])
        for e in a[i]:
            idx[e].append(i)

    ans = 0
    for _ in range(n):
        b = int(input()) - 1
        for id in idx[b]:
            cnt[id] -= 1
            if cnt[id] == 0:
                ans += 1
        print(ans)

