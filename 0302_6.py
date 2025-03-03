def fib(num):
    if num == 0:
        return 1
    return fib(num - 1)

print(fib(35))