n, m = map(int, input().split())

if n < 7:
    print("breakfast")
elif 7 <= n < 13:
    if n == 7:
        if m == 0:
            print("breakfast")
        else:
            print("lunch")
    else:
        print("lunch")
elif 13 <= n < 19:
    if n == 13:
        if m == 0:
            print("lunch")
        else:
            print("dinner")
    else:
        print("dinner")
else:
    print("breakfast")