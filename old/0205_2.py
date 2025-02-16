n, s, k = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

total = 0
for i in range(n):
    total += l[i][0] * l[i][1]

print(total + k if total < s else total)
