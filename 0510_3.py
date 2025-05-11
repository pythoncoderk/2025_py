a, b = map(int, input().split())
flag = False
for i in range(a, b + 1):
    if 100 % i == 0:
        flag = True

print("Yes" if flag else "No")
