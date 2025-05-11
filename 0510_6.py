n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                if l[i] + l[j] + l[k] == 1000:
                    print("Yes")
                    exit()
print("No")
