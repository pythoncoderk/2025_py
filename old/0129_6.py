n = int(input())
l = list(map(int, input().split()))

x = max(l)

max_count = l.count(x)

print(1 if max_count >= 2 and l[0] == x else 0 if max_count == 1 and l[0] == x else x - l[0] + 1)