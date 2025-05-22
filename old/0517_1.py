a, b, c, d = map(int, input().split())

if a > c:
    print("Yes")
else:
    if a == c:
        if b > d:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
