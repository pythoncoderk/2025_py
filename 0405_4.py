n, m = map(int, input().split())

ans = n
total = [1, n,]
for i in range(m-1):
    ans = ans * n
    total.append(ans)

print(sum(total) if sum(total) <= 1000000000 else "inf")