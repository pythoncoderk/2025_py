# from bisect import bisect
import bisect
n = int(input())
l = list(map(int, input().split()))

count = 0
for i in l:
    count += bisect.bisect_right(l, i * 2)

print(count)