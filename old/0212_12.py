n = int(input())

count = 0
flag = True

for _ in range(n):
    x = input()
    if not flag:
        print("No")
        exit()
    if x == "sweet":
        count += 1
        if count >= 2:
            flag = False
    else:
        count = 0

print("Yes")