n = int(input())
l = list(map(int, input().split()))

flag = True
diff = 0
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        flag = True
    else:
        flag = False
        break


print("Yes" if flag else "No")