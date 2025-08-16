n = int(input())
l = list(map(int, input().split()))

print(n)
print(l)

for i in range(n-1):
    for j in range(n-1):
        total = 0
        for k in range(i, j+1):
            total += l[j]
        print(total)




