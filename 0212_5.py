n, m = map(int, input().split())
l = list(map(int, input().split()))


for i in range(n):
    m -= l[i]
    if m < 0:
        print(i)
        exit()
print(n)