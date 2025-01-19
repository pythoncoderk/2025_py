n = int(input())

l = [input() for i in range(n)]

print(l.pop())

for i in range(len(l) - 1, -1, -1):
    print(l[i])