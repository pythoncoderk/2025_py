n = int(input())
s = 0
for i in range(n):
    x = input()
    if x == "ball":
        print("ball")
    else:
        s += 1
        print("strike!")
        print(s)