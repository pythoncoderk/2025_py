n, m = map(int, input().split())
x = int(input())

count = 1
while True:
    if n * count <= 1500:
        print(n * count, abs(x - n * count))
    else:
        break
    count += 1