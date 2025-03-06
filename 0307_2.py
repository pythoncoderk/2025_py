n = int(input())

count = 0
bitmask = 1
while bitmask <= n:
    if n & bitmask != 0:
        count += 1
    bitmask *= 2

print(count)
