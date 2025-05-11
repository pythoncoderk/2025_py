n, x = map(int, input().split())
l = list(map(int, input().split()))
flag = False
for i in l:
    if i == x:
        flag = True

print("Yes" if flag else "No")
