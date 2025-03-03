n = int(input())
b = 0
s = 0
for i in range(n):
    x = input()
    if x == "ball":
        b += 1
        if b >= 4:
            print("fourball!")
        else:
            print("ball!")
    else:
        s += 1
        if s >= 3:
            print("out!")
        else:
            print("strike!")