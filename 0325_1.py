n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

ans = 0
count = 0
for i in l:
    if count == i:
        ans += 1
    else:
        count = i
        ans = 0
    if ans == 2:
        break

print("Yes" if ans == 2 else "No")