n = int(input())
s = input()

sl = (n + 1) // 2

if n % 2 == 0:
    print("No")
    exit()

if s[(sl - 1)] != "/":
    print("No")
    exit()

for i in range(0, sl-1):
    if s[i] != "1":
        print("No")
        exit()

for i in range(sl, n):
    if s[i] != "2":
        print("No")
        exit()

print("Yes")