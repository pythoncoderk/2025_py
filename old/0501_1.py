n, x = map(int, input().split())
l = list(map(int, input().split()))

print(n, x)
print(l)

ans = 0

for i in range(1 << x):
    print(i)