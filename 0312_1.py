n = int(input())

count = 0
bitmask = 1
while bitmask <= n:
    if bitmask & n != 0:
        count += 1
    bitmask *= 2

print(count)