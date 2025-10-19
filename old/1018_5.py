n, k = map(int, input().split())
s = input()

l = []
for i in range(n-k+1):
    l.append(s[i:k+i])
l2 = []
for i in range(len(l)):
    l2.append(l.count(l[i]))

l_max = max(l2)
l3 = []
for i in range(len(l)):
    if l2[i] == l_max:
        l3.append(l[i])
l4 = set(l3)
l5 = list(l4)
l5.sort()
print(l_max)
print(*l5)
