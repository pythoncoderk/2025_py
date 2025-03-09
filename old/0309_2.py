n = int(input())
l = [0 for i in range(101)]


for i in range(n):
    l2 = list(map(int, input().split()))
    if l2[0] == 2:
        print(l.pop(0))
    else:
        l.insert(0, l2[1])

