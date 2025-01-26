n, m = map(int, input().split())

l1 = list(map(int, input().split()))

l2 = list(map(int, input().split()))

ans = 0

for i in l2:
    ans += l1[i - 1]

print(ans)