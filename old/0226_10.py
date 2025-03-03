n = int(input())

s = 0
for i in range(n):
    x = input()
    if x == "ball":
        print("ball")
    else:
        s += 1
        if s <= 2:
            print("strike!")
        else:
            print("out!")