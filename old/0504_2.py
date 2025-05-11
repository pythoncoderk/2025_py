def fib_dp(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        memo = [None] * (n + 1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

for i in range(35):
    print(fib_dp(i))