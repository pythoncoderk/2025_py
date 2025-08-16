n = int(input())
ans = 0
ans_str = ""
for i in range(n):
    x, y = map(str, input().split())
    ans += int(y)
    if ans > 100:
        print("Too Long")
        exit()
    else:
        for j in range(int(y)):
            ans_str += x

print(ans_str)