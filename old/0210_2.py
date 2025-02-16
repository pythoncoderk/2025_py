n = int(input())
l = list(map(int, input().split()))

l2 = []
for i in range(n - 1):
    l2.append(l[i] * l[i+1])

print(*l2)