from bisect import bisect
N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    # A の要素のうち a / 2 以下のものの個数を合計する
    ans += bisect(A, a // 2)
print(ans)