import bisect

n = int(input())
l = list(map(int, input().split()))

count = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i] * 2 <= l[j]:
            count += len(l) - j
            break

print(count)
