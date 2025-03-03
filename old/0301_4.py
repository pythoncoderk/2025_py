n = int(input())
l = list(map(int, input().split()))

flag = True
for i in range(len(l)-1):
    if l[i] >= l[i + 1]:
        flag = False

print("Yes" if flag else "No")