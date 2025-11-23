n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort()

for i in range(n):

    for j in range(m):
        if l1[i] <= l2[j]:
            l2[j] = 0
            l1[i] = 0
            break

if sum(l1) == 0:
    print("YES")
else:
    print("NO")