def sum1(n):
    s = 1
    for i in range(2, n + 1):
        s = s + 1
    return s

def sum2(n):
    return n * (n + 1) // 2