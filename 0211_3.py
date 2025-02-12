n = int(input())
x = 1
count = 0
while True:
    if n < x:
        print(count + 1)
        break
    else:
        x = (x * 2) + 1
        count += 1
