l = list(map(int, input().split()))

flag = True

for i in range(len(l) - 1):
    if l[i] <= l[i + 1]:
        flag = True
    else:
        flag = False
        break

if not flag:
    print("No")
    exit()

for i in l:
    if 100 <= i <= 675 and i % 25 == 0:
        flag = True
    else:
        flag = False

print("Yes" if flag else "No")