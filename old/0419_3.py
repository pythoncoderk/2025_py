n = int(input())

l = []
for i in range(n):
    l2 = list(map(int, input().split()))
    if l2[0] == 1:
        l.append(l2[1])
    else:
        print(l.pop(0))
