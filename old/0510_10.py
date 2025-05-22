n = input()

x = n[::-1]

total = 0
m = 1
for i in range(len(x)):
    if x[i] == "1":
        total += m
    m *= 2
print(total)
