n = int(input())
l = list(map(int, input().split()))
x = int(input())

for i in range(n):
    if l[i] == x:
        print("Yes")
        exit()
print("No")