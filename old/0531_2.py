n = int(input())
l = list(map(int, input().split()))

set_l = set(l)

ans = sorted(set_l)

print(len(ans))
print(*ans)