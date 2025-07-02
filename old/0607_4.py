n = int(input())
t = input()
a = input()

flag = False
for i in range(n):
    if t[i] == "o" and a[i] == "o":
        flag = True

print("Yes" if flag else "No")

