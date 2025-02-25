l = list(map(int, input().split()))
l2 = l[:]
l2.sort()

for j in range(len(l)-1, -1, -1):
    if l[j-1] > l[j]:
        l[j-1], l[j] = l[j], l[j-1]
        break

print("Yes" if l == l2 else "No")