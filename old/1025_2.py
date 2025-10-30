n, m = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    ans = 0
    for j in range(n):
        if i != j:
            ans += l[j]
    if ans == m:
        print("Yes")
        exit()
print("No")
