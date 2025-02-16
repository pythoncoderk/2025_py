s = input()

x = int(s[-3:])

if 1 <= x <= 349 and x != 316:
    print("Yes")
else:
    print("No")