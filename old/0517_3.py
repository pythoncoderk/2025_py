n = int(input())
x = 512

for i in range(10):
    print((n // x) % 2, end="")
    x //= 2
