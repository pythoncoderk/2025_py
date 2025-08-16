import numpy as np

a = int(input())
n = int(input())
total = 0
for i in range(1, n+1):
    x = np.base_repr(i, a)
    if str(i) == str(i)[::-1] and x == x[::-1]:
        total += i

print(total)
