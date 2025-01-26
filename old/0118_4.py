import math

x = int(input())
count = 2
while True:
    ans = math.factorial(count)
    if x == ans:
        print(count)
        break
    else:
        count += 1


