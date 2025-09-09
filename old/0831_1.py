n = int(input())
l = []
for i in range(n):
    l.append(input())
l2 = list(map(str, input().split()))

x = int(l2[0])
s = l2[1]

print("Yes" if l[x - 1] == s else "No")
