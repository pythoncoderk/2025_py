def calc(n):
    if n == 0:
        return 1
    return n * calc(n - 1)

n = int(input())
print(calc(n))