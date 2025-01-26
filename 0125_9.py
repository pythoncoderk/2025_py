l = list(map(int, input().split()))

count_1 = 0
for i in range(len(l)-1):
    if l[i] < l[i + 1]:
        count_1 += 1

if count_1 == len(l)-1:
    print("No")
    exit()

for i in range(len(l)-1, 0, -1):
    if l[i] < l[i - 1]:
        l[i], l[i-1] = l[i-1], l[i]
        break

count = 0
for i in range(len(l)-1):
    if l[i] < l[i + 1]:
        count += 1

print("Yes" if count == len(l)-1 else "No")