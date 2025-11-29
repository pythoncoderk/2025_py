x, y, z = map(int, input().split())


for i in range(1000):
    if y * z == x:
        print("Yes")
        exit(0)
    else:
        y += 1
        x += 1

print("No")