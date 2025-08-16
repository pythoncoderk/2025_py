n = int(input())
x = int(input())

ans = n
for i in range(6):

    ans += int(n * (x / 100))
    n = int(n * (x / 100))

print(int(ans))