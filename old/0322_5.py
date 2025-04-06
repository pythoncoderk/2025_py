import itertools

n = int(input())
l = list(map(int, input().split()))

l2 = itertools.groupby(l)

for key, group in range(len(l2)):
    print(f"{key}: {list(group)}")