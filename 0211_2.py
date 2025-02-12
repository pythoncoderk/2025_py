n = int(input())
l = list(map(int, input().split()))

count = -1

for i in range(1, n):
    if l[0] < l[i]:
        count = i + 1
        break

print(count)