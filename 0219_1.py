l = list(map(int, input().split()))

for i in range(len(l)):
    for j in range(len(l)):
        if i != j and l[i] != -1 and l[j] != -1:
            if l[i] == l[j]:
                l[i] = -1
                l[j] = -1
                break

print(l.count(-1) // 2)
