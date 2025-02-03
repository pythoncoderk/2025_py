n = int(input())
l = list(map(str, input().split()))
s = set(l)

print("Yes" if len(s) == 1 else "No")