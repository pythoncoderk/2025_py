a, b = map(int, input().split())

flag = True

if a % 3 != 0:
    if a + 1 == b:
        flag = True
        print("Yes")
        exit()
    if a + 3 == b:
        flag = True
        print("Yes")
        exit()
    else:
        print("No")
        exit()
else:
    if not (a % 3 == 0 and b % 3 == 0):
        flag = False

print("Yes" if flag else "No")
