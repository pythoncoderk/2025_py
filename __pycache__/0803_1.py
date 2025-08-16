n = int(input())
l = list(map(int, input().split()))
x = int(input())

for i in l:
    if i == x:
        print("Yes")
        exit()
print("No")