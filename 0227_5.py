n = int(input())
l = list(map(int, input().split()))

x = 0
for i in range(len(l)):
    if i == 0:
        x += l[i]
    else:
        if l[i] < 0:
            x += l[i]
        else:
            if abs(x) < l[i]:
                print("NO")
                exit()
            else:
                x += l[i]
print("YES")


