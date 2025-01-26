n = int(input())

l = [input() for i in range(n)]

print(l.pop())

for i in range(len(l)):
    print(l[-(i + 1)])