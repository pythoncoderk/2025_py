n = input()

le = len(n)

m = int(n)

bitm = 1
count = 0
for i in range(1, le+1):
    if m & (i * bitm) == 1:
        count += 1
    bitm *= 2
print(count)