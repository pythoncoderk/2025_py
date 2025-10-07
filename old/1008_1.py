n = int(input())
for i in range(n):
    a = input()
    b = input()
    a2 = sorted(a)
    b2 = sorted(b)
    if a2 == b2:
        print("Yes")
    else:
        print("No")