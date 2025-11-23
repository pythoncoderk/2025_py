N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

j = 0

for x in a:
    while j < M and b[j] < x:
        j += 1
    if j == M:
        print("NO")
        exit()

    j += 1
print("YES")


