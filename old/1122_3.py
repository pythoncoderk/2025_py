n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort()

l1_min = min(l1)
for i in range(m):
    if l2[i] < l1_min:
        l2[i] = 0
    else:
        break

i = 0
while True:
    if l2[i] == 0:
        l2.pop(i)
    else:
        break

if len(l1) > len(l2):
    print("NO")
    exit()

for i in range(n):
    if l1[i] > l2[i]:
        print("NO")
        exit()

print("YES")