n = input()
x = n[::-1]
total = 0
num = 1
for i in x:
    if i == "1":
        total += num * 1
        num *= 2

print(total + num if x[-1] == "1" else total)




