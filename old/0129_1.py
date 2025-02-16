a, b = map(int, input().split())

if b % 3 != 0 and a % 3 != 0:
    if a + 1 == b:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if a % 3 == 0:
    if a + 3 == b:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if a + 3 == b:
    print("Yes")
    exit()
else:
    print("No")
    exit()

