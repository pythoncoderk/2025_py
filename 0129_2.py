a, b = map(int, input().split())

if a % 3 == 0:
    print("No")
else:
    if a + 1 == b:
        print("Yes")
    else:
        print("No")