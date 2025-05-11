check = 12
n = len(bin(check)) - 2
print(bin(check))

for i in range(n):
    if check & (1 << i):
        print("yes")
    else:
        print("no")

