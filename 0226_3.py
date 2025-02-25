d = input()
n = int(input())
for i in range(n):
    x = input()
    if x == d:
        print("first")
    elif str(int(x) - 1) == d or str(int(x) + 1) == d:
        print("adjacent")
    elif d[-4:] == x[-4:]:
        print("second")
    elif d[-3:] == x[-3:]:
        print("third")
    else:
        print("blank")