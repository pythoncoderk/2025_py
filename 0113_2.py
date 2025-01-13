a, b = map(int, input().split())

while True:
    if a > b:
        a = a % b
    elif b == 0 or a == 0:
        print(max(a, b))
        break
    else:
        b = b % a