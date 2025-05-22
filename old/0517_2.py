n, k = map(int, input().split())
l = list(map(int, input().split()))

x = 1
ans = 0
for i in range(n):
    ans = x * l[i]
    if len(str(ans)) > k:
        x = 1
    else:
        x = ans
print(x)