n = int(input())
l = list(map(int, input().split()))
x = int(input())

ans = 0
for i in range(n):
    if l[i] == x:
        ans += 1

print("Yes" if ans >= 1 else "No")