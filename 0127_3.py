f = input()
n = int(input())
l = [input() for i in range(n)]

for i in range(n):
    if l[i] == f:
        print("first")
    elif int(l[i]) - 1 == int(f) or int(l[i]) + 1 == int(f):
        print("adjacent")
    elif f[-4:] == l[i][-4:]:
        print("second")
    elif f[-3:] == l[i][-3:]:
        print("third")
    else:
        print("blank")