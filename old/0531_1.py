n, s = map(int, input().split())
l = list(map(float, input().split()))

if l[0] >= s + 0.5:
    print("No")
    exit()

for i in range(n - 1):
    # xxx = l[i+1] - l[i]
    # yyy = s + 0.5
    if l[i + 1] - l[i] >= s + 0.5:
        print("No")
        exit()

print("Yes")
