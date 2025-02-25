n = int(input())

l = [input() for i in range(n)]
l.sort()

for i in range(n):
    for j in range(n-1, i, -1):
        if len(l[j]) < len(l[j-1]):
            l[j], l[j-1] = l[j-1], l[j]

print("".join(l))