n = int(input())
s = 0
b = 0

for i in range(n):
    x = input()
    if x == "ball":
        b += 1
        if b <= 3:
            print("ball!")
        else:
            print("fourball!")
    else:
        s += 1
        if s <= 2:
            print("strike!")
        else:
            print("out!")