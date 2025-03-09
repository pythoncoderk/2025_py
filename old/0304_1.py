n = int(input())

count = 0
while True:
    if n == 0:
        break
    else:
        if n % 2 != 0:
            count += 1
        n //= 2

print(count)