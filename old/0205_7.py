n = int(input())

l = [list(map(int, input().split())) for i in range(n)]

t = 0
a = 0
for i in range(n):
    t += l[i][0]
    a += l[i][1]

if t == a: print("Draw")
elif t > a: print("Takahashi")
else: print("Aoki")