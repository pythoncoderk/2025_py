n = int(input())
flag = False
count = 0
for i in range(n):
    x = input()
    if x == "login":
        flag = True
    elif x == "logout":
        flag = False

    if not flag:
        if x == "private":
            count += 1

print(count)

