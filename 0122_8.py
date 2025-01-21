n = int(input())

s = input()

maru = 0
batsu = 0

for i in s:
    if i == "o":
        maru += 1
    elif i == "x":
        batsu += 1

print("Yes" if maru >= 1 and batsu == 0 else "No")