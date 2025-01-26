n = int(input())

min_l = (n // 5) * 5

max_l = ((n // 5) + 1) * 5

print(max_l if max_l - n <= n - min_l else min_l)