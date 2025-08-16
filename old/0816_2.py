
n = int(input())

l_1 = []
for i in range(n):
    l = list(map(int, input().split()))
    if l[0] == 1:
        l_1.append(l[1])
    else:
        if len(l_1) != 0:
            l_1.sort()
            print(l_1.pop(0))