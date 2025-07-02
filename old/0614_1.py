n = int(input())
l = list(map(int, input().split()))
m = int(input())
count = 0
for i in l:
    if i >= m:
        count += 1

print(count)
