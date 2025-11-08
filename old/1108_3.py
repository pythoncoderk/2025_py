x = int(input())
n = int(input())
l = list(map(int, input().split()))
q = int(input())
l2 = []
for i in range(q):
    y = int(input())
    l2.append(y)
ans = x
l3 = []
for i in range(q):
    if l2[i] not in l3:
        l3.append(l2[i])
        print(ans + l[l2[i]-1])
        ans += l[l2[i]-1]
    else:
        l3.pop(l3.index(l2[i]))
        print(ans - l[l2[i]-1])
        ans -= l[l2[i]-1]