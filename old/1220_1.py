n = int(input())
a, b = map(int, input().split())

l = list(map(int, input().split()))

ans = 0

for i in l:
    if i >= a:
        ans += i

print("silver" if ans >= 3 and sum(l) >= b else "bronze")